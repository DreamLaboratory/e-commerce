from django.core.management.base import BaseCommand, CommandError
from ...models import City
import yaml

class Command(BaseCommand):
    help='imoprt region from a yaml file'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
            'Imoprt region ....wait..'
            )
        )
        City.objects.all().delete()
        try:
            with open('src/apps/common/fixtures/cities.yaml','r') as yaml_file:
                data=yaml.safe_load(yaml_file)
                i=0
                for item in data:
                    City.objects.create(
                        name=item['name_uz'],region_id=item['region_id']
                    )
                    i=i+1
        except FileNotFoundError as e:
            raise CommandError('File City yaml doesn\'t exists ')
        self.stdout.write(self.style.SUCCESS(f'{str(i)} cities successfully imported'))
        