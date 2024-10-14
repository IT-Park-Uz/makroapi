import os
import requests
from tablib import Dataset
from django.core.files.base import ContentFile


def parse_animals_from_excel(file_path):
    # Чтение Excel файла
    with open(file_path, 'rb') as f:
        dataset = Dataset().load(f.read(), format='xlsx')

    animals_data = []

    for row in dataset.dict:
        # Сохранение изображения
        image_url = row['Картинка']
        if image_url:
            # Получаем имя файла
            image_name = os.path.basename(image_url)
            # Загружаем изображение
            response = requests.get(image_url)
            image_content = ContentFile(response.content)

            # Сохраняем данные в список
            animals_data.append({
                "picture": image_content,
                "image_name": image_name,
                "name_uz": row['Имя на узб'],
                "name_ru": row['Имя на русском'],
                "short_text": row['Сокращенный текст'],
                "short_text_uz": row['Перевод на узбекский'],
                "role_ru": row['Роль, рус.яз.'],
                "role_uz": row['Роль, уз.яз.'],
                "story_ru": row['История персонажа, рус'],
                "story_uz": row['История персонажа, узб'],
                "facts_ru": row['Интересные факты, рус.'],
                "facts_uz": row['Интересные факты, узб'],
            })

    return animals_data
