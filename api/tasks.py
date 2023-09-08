import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from tablib import Dataset

from common.product.models import File, Product, Category

User = get_user_model()


@shared_task(name='create_products')
def create_products(file_id):
    newProducts = []
    updateProducts = []
    file = File.objects.filter(id=file_id).first()
    if file is None:
        return {'error': "File does not exists"}
    try:
        dataset = Dataset()
        imported_data = dataset.load(file.file.read(), format='xlsx')
    except Exception as e:
        file.delete()
        return {'error': str(e)}
    for data in imported_data:
        category, created = Category.objects.get_or_create(title=data[5])
        try:
            code = data[4].split(',')[-1].strip()
            title = " ".join(data[4].split(',')[:-1]).strip()
            oldPrice = data[6]
            newPrice = data[7]
            percent = round((oldPrice / newPrice) - 1, 1) * 100

            product = Product.objects.filter(code=code, title=title).first()
            status = 1 if product.oldPrice <= oldPrice and newPrice < product.oldPrice else 2
            if product:
                updateProducts.append(Product(
                    id=product.id,
                    category=category,
                    code=product.code,
                    title=product.title,
                    oldPrice=oldPrice,
                    newPrice=newPrice,
                    percent=percent,
                    startDate=data[2],
                    endDate=data[3],
                    status=status
                ))
            else:
                newProducts.append(Product(
                    category=category,
                    code=code,
                    title=title,
                    newPrice=newPrice,
                    oldPrice=oldPrice,
                    percent=percent,
                    startDate=data[2],
                    endDate=data[3],
                    status=status
                ))
        except Exception as e:
            print("Error", e)
            continue
    if newProducts:
        Product.objects.bulk_create(newProducts)
    if updateProducts:
        Product.objects.bulk_update(updateProducts,
                                    fields=['category', 'code', 'title', 'newPrice', 'oldPrice', 'percent', 'startDate',
                                            'endDate', 'status'])
    return {"message": "Product has updated and created successfully"}


@shared_task(name='deleteExpiredProducts')
def deleteExpiredProducts():
    products = Product.objects.filter(endDate=datetime.datetime.now().date() + datetime.timedelta(days=1))
    for p in products:
        p.status = 2
        p.save()
    return {"message": "Expired product status has changed successfully"}
