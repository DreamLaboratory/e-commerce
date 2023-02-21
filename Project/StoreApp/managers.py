from django.db import models


class ProductVariantsManager(models.Manager):

    def colors(self):
        from .models.variants import CategoryVariants
        return self.filter(variant_category=CategoryVariants.COLOR)

    def size(self):
        from .models.variants import CategoryVariants
        return self.filter(variant_category=CategoryVariants.SIZE)
