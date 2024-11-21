# management/commands/import_animals.py
from django.core.management.base import BaseCommand
from common.ferma.models import Toys
from common.ferma.parsers import parse_animals_from_excel  # Импорт функции для парсинга Excel
import os


class Command(BaseCommand):
    help = 'Import animal data from Excel file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help="Path to the Excel file with animal data")

    def handle(self, *args, **options):
        file_path = options['file_path']

        # Проверка существования файла
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f'File "{file_path}" does not exist.'))
            return

        # Парсим данные из Excel файла
        animals_data = parse_animals_from_excel(file_path)

        for data in animals_data:
            # Сохраняем изображение в базе данных
            animal = Toys.objects.update_or_create(
                name=data['name'],
                defaults={
                    'picture': data['picture'],  # Это объект ContentFile
                    'name_uz': data['name_uz'],
                    'short_description': data['short_text'],
                    'short_description_uz': data['short_text_uz'],
                    'role': data['role_ru'],
                    'role_uz': data['role_uz'],
                    'description': data['story_ru'],
                    'description_uz': data['story_uz'],
                    'facts': data['facts_ru'],
                    'facts_uz': data['facts_uz'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported animals data!'))
