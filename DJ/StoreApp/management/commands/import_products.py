import yaml
from django.core.management.base import BaseCommand ,CommandError
from ...models.product import Product



class Command(BaseCommand):
    help = "Import products from a yaml file"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.HTTP_NOT_MODIFIED(
                "Import products... wait...",
            )
        )
        Product.objects.all().delete()
        try:
            with open(
                "HomeApp/fixtures/products.yaml",
                "r",
            ) as yaml_file:
                data = yaml.safe_load(yaml_file)
                i = 0
                for item in data:
                    print(item)
                    Product.objects.create(
                        name=item["name"],
                        descriptions=item["descriptions"],
                        quantity=item["quantity"],
                        price=item["price"],
                        is_available=item["is_available"],
                    )
                    i += 1
        except FileNotFoundError as e:
            raise CommandError("File products yaml doesn't exists") from e

        self.stdout.write(self.style.SUCCESS(f"{str(i)} products successfully imported"))

