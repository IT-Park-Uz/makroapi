import os
import datetime
import shutil
import zipfile

from datetime import timedelta

from celery import shared_task
from django.core.files import File as CoreFile
from django.contrib.auth import get_user_model
from django.conf import settings
from tablib import Dataset

from common.discount.models import Discount, DiscountStatus
from common.product.models import File, Product, Category, ProductStatus, TopCategory

User = get_user_model()


@shared_task(name='deleteProducts')
def deleteProducts():
    files = File.objects.all()
    files.delete()
    products = Product.objects.all()
    products.delete()


@shared_task(name='createProducts')
def createProducts(file_id):
    file = File.objects.filter(id=file_id).first()
    message = "Begin\n"
    try:
        if file is None:
            message += "File does not exists\n"
            raise Exception(message)
        try:
            dataset = Dataset()
            imported_data = dataset.load(file.file.read(), format='xlsx')
        except Exception as e:
            message += "Error reading dataset\n"
            raise Exception(message)
        target_directory = os.path.join(settings.MEDIA_ROOT, 'extracted_images')
        os.makedirs(target_directory, exist_ok=True)
        with zipfile.ZipFile(file.images_file.path, 'r') as zip_ref:
            zip_ref.extractall(target_directory)
        image_files = {}
        for root, _, files in os.walk(target_directory):
            for file_name in files:
                if file_name.endswith('.png'):
                    code = os.path.splitext(file_name)[0]
                    image_files[code] = os.path.join(target_directory, file_name)

        total = 0
        processed = 0
        for num, data in enumerate(imported_data):
            code = data[0]
            if code is None:
                continue
            total += 1
            code = str(int(code))
            image_file_path = image_files.get(code)
            category, created = Category.objects.get_or_create(title=data[6], title_ru=data[7])
            top_category = None
            if data[10] and data[11]:
                t1 = data[10].strip()
                t2 = data[11].strip()
                top_category, created = TopCategory.objects.get_or_create(title=t1, title_ru=t2)
            title = data[4].split(',')[0]
            title_ru = data[5].split(',')[0]
            oldPrice = data[8]
            newPrice = data[9]
            region_str = data[12].strip()
            region_dict = {
                "Вся сеть": 3,
                "Ташкент": 1,
                # "Долина": 2
            }
            percent = ((oldPrice - newPrice) / oldPrice) * 100
            start_date = data[2]
            end_date = data[3]
            # Check if the data is a datetime object, if not, convert it to a string
            if isinstance(start_date, int):
                start_date = datetime.datetime(1899, 12, 30) + timedelta(days=start_date)

            if isinstance(end_date, int):
                end_date = datetime.datetime(1899, 12, 30) + timedelta(days=end_date)
            try:
                product = Product(
                    code=code,
                    category=category,
                    top_category=top_category,
                    title=title,
                    title_ru=title_ru,
                    oldPrice=oldPrice,
                    newPrice=newPrice,
                    percent=round(percent),
                    startDate=start_date,
                    endDate=end_date,
                    status=2,
                    region_id=region_dict[region_str],
                    order=num+1
                )

                if image_file_path:
                    with open(image_file_path, 'rb') as image_file:
                        product.photo.save(f'{code}.png', CoreFile(image_file), save=True)
                        processed += 1
                        product.status = ProductStatus.HasDiscount if settings.STAGE == 'prod' else ProductStatus.NoDiscount
                product.save()
            except Exception as e:
                message += f"Error saving product {code}: {str(e)}\n"
                file.save()
        file.total = total
        file.processed = processed
        file.save()
        for file_or_folder in os.listdir(target_directory):
            file_or_folder_path = os.path.join(target_directory, file_or_folder)
            if os.path.isfile(file_or_folder_path):
                os.unlink(file_or_folder_path)
            else:
                shutil.rmtree(file_or_folder_path)
    except Exception as e:
        message += f"Some error for exception: {e}\n"
    file.message = message
    file.save()
    return {"message": message}


@shared_task(name='dailyChecking')
def dailyChecking():
    today = datetime.datetime.now().date()
    today_end = today - timedelta(days=1)
    updateProducts = []
    updateDiscounts = []

    for p in Product.objects.all():
        if p.startDate > today or p.startDate < today < p.endDate:
            continue
        elif p.endDate == today_end:
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
        elif d.endDate == today_end:
            updateDiscounts.append(Discount(
                id=d.id,
                status=DiscountStatus.ARCHIVE
            ))
    if updateProducts:
        Product.objects.bulk_update(updateProducts, fields=['status'])

    if updateDiscounts:
        Discount.objects.bulk_update(updateDiscounts, fields=['status'])
    return {"message": "Status has changed successfully"}
