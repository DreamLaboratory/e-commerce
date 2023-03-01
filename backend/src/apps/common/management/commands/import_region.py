import yaml
from django.core.management.base import BaseCommand, CommandError

from ...models import Region
from ...tg_alert import tg_alert

class Command(BaseCommand):
    help = "Import regions from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import regions... wait...",
            )
        )
        Region.objects.all().delete()
        try:
            with open(
                "src/apps/common/fixtures/region.yaml",
                "r",
            ) as file:
                data = yaml.safe_load(file)
                i = 0
                for item in data:
                    Region.objects.create(name=item["name_uz"])
                    i += 1
        except FileNotFoundError as e:
            tg_alert.custom_alert(e)
            raise CommandError("File regions yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} cities successfully imported"))