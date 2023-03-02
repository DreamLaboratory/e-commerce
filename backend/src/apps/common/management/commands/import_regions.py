import yaml
from django.core.management.base import BaseCommand, CommandError
from ...models import Region

class Command(BaseCommand):
    help='imoprt region from a yaml file'

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
            'Imoprt region ....wait..'
            )
        )
        Region.objects.all().delete()
        try:
            with open('src/apps/common/fixtures/regions.yaml','r') as yaml_file:
                data=yaml.safe_load(yaml_file)
                i=0
                for item in data:
                    Region.objects.create(
                        name=item['name_uz']
                    )
                    i=i+1
        except FileNotFoundError as e:
            raise CommandError('File Region yaml doesn\'t exists ')
        self.stdout.write(self.style.SUCCESS(f'{str(i)} region successfully imported'))
        
 
