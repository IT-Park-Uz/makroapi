import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from tablib import Dataset

from common.discount.models import Discount, DiscountStatus
from common.product.models import File, Product, Category, ProductStatus

User = get_user_model()


@shared_task(name='deleteProducts')
def deleteProducts():
    files = File.objects.all()
    files.delete()
    products = Product.objects.all()
    products.delete()


@shared_task(name='createProducts')
def createProducts(file_id):
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
        category, created = Category.objects.get_or_create(title=data[6], title_ru=data[7])
        try:
            code = data[0]
            product = Product.objects.filter(code=code).first()

            title = " ".join(data[4].split(',')[:-1]).strip()
            title_ru = " ".join(data[5].split(',')[:-1]).strip()
            oldPrice = data[8]
            newPrice = data[9]
            percent = ((oldPrice - newPrice) / oldPrice) * 10
            if product:
                if newPrice != oldPrice:
                    status = 1
                else:
                    status = 2
                    percent = 0
                    newPrice = oldPrice
                updateProducts.append(Product(
                    id=product.id,
                    category=category,
                    code=product.code,
                    title=product.title,
                    title_ru=product.title_ru,
                    oldPrice=oldPrice,
                    newPrice=newPrice,
                    percent=percent,
                    startDate=data[2],
                    endDate=data[3],
                    status=status
                ))
            else:
                status = 1 if newPrice != oldPrice else 2
                newProducts.append(Product(
                    category=category,
                    code=code,
                    title=title,
                    title_ru=title_ru,
                    newPrice=newPrice,
                    oldPrice=oldPrice,
                    percent=percent,
                    startDate=data[2],
                    endDate=data[3],
                    status=status
                ))
        except Exception as e:
            continue
    if newProducts:
        Product.objects.bulk_create(newProducts)
    if updateProducts:
        Product.objects.bulk_update(updateProducts,
                                    fields=['category', 'code', 'title', 'title_uz', 'title_ru', 'newPrice', 'oldPrice',
                                            'percent', 'startDate', 'endDate', 'status'])
    return {"message": "Product has updated and created successfully"}


@shared_task(name='dailyChecking')
def dailyChecking():
    today = datetime.datetime.now().date()
    updateProducts = []
    updateDiscounts = []

    for p in Product.objects.all():
        if p.startDate > today or p.startDate < today < p.endDate:
            continue
        elif p.endDate == today:
            updateProducts.append(Product(
                id=p.id,
                status=ProductStatus.NoDiscount
            ))
        elif p.startDate == today:
            updateProducts.append(Product(
                id=p.id,
                status=ProductStatus.HasDiscount
            ))

    for d in Discount.objects.all():
        if d.startDate > today or d.startDate < today < d.endDate:
            continue
        elif d.endDate == today:
            updateDiscounts.append(Discount(
                id=d.id,
                status=DiscountStatus.ARCHIVE
            ))
        elif d.startDate == today:
            updateDiscounts.append(Discount(
                id=d.id,
                status=DiscountStatus.ACTIVE
            ))
    if updateProducts:
        Product.objects.bulk_update(updateProducts, fields=['status'])

    if updateDiscounts:
        Discount.objects.bulk_update(updateDiscounts, fields=['status'])
    return {"message": "Status has changed successfully"}
