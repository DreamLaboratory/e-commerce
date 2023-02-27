from django.db import models


class ProductVariansManager(models.Manager):
    def colors(self):
        from .models.variants import VariantChoises

        return self.filter(product_variant=VariantChoises.COLOR)

    def sizes(self):
        from .models.variants import VariantChoises

        return self.filter(product_variant=VariantChoises.SIZE)