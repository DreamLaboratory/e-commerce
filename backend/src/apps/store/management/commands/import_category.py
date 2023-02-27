from django.core.management.base import BaseCommand
from ...models.category import Category

import yaml


class Command(BaseCommand):
    help = 'Import category....'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()

        try:
            with open('src/apps/common/import_category/category.yaml', 'r') as yaml_file:
                data = yaml.safe_load(yaml_file)
                for item in data:
                    Category.objects.create(name=item['name'])
            self.stdout.write(self.style.SUCCESS('Successfully ADD category'))

        except:
            self.stdout.write(self.style.WARNING('File not found'))
