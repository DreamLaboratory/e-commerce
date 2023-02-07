from django.core.management import BaseCommand,CommandError
import yaml
from ...models.category import Category



class Command(BaseCommand):
    help = 'import category process'


    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import Category wait ... minutes"
            )
        )
        # Category.objects.all().delete()
        try:
            with open(
                    "HomeApp/fixtures/category.yaml",
                    "r"
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    print(item)
                    Category.objects.create(
                        name = item['name'],
                        descriptions = item['descriptions'],
                    )
                    i+=1

        except FileNotFoundError as error:
            raise CommandError("File category yaml doesn't exists") from error

        self.stdout.write(self.style.SUCCESS(f"{str(i)} category successfully imported"))


