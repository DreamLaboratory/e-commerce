import yaml
from ...models.product import Product
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Import  Product from yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "IMPORTO PRODUCT......wait....",
            )
        )
        Product.objects.all().delete()

        try:
            with open(
                "src/apps/common/fixtures/product.yaml",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    Product.objects.create(
                        name=item["name"],
                        description=item["description"],
                        price=item["price"],
                        stock=item["stock"],
                        is_availabel=item["is_availabel"],
                    )
                    i = i + 1
        except FileNotFoundError as e:
            raise CommandError("File products yammldoesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} products successful create"))
