import datetime

from celery import shared_task
from django.contrib.auth import get_user_model
from tablib import Dataset

from common.discount.models import Discount, DiscountStatus
from common.news.models import News, NewsStatus
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
        category, created = Category.objects.get_or_create(title=data[5])
        try:
            code = data[4].split(',')[-1].strip()
            title = " ".join(data[4].split(',')[:-1]).strip()
            oldPrice = data[6]
            newPrice = data[7]
            percent = round((oldPrice / newPrice) - 1, 1) * 100

            product = Product.objects.filter(code=code, title=title).first()
            if product:
                status = 1 if product.oldPrice <= oldPrice and newPrice < product.oldPrice else 2
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
                status = 2
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
            continue
    if newProducts:
        Product.objects.bulk_create(newProducts)
    if updateProducts:
        Product.objects.bulk_update(updateProducts,
                                    fields=['category', 'code', 'title', 'newPrice', 'oldPrice', 'percent', 'startDate',
                                            'endDate', 'status'])
    return {"message": "Product has updated and created successfully"}


@shared_task(name='dailyChecking')
def dailyChecking():
    today = datetime.datetime.now().date()
    updateProducts = []
    updateDiscounts = []
    updateNews = []

    for p in Product.objects.all():  # filter(startDate__lt=today, endDate__gt=today):
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

    for d in Discount.objects.all():  # filter(startDate__lt=today, endDate__gt=today):
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

    for n in News.objects.all():  # filter(startDate__lt=today, endDate__gt=today):
        if n.startDate > today or n.startDate < today < n.endDate:
            continue
        elif n.endDate == today:
            updateNews.append(News(
                id=n.id,
                status=NewsStatus.ARCHIVE
            ))
        elif n.startDate == today:
            updateNews.append(News(
                id=n.id,
                status=NewsStatus.ACTIVE
            ))
    if updateProducts:
        Product.objects.bulk_update(updateProducts, fields=['status'])

    if updateDiscounts:
        Discount.objects.bulk_update(updateDiscounts, fields=['status'])

    if updateNews:
        News.objects.bulk_update(updateNews, fields=['status'])
    return {"message": "Status has changed successfully"}
