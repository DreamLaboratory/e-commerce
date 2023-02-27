from django.db import models


class ProductVariantManager(models.Manager):
    def colors(self):
        from ..common.choices import VariantCategory

        return self.filter(variant_category=VariantCategory.COLOR)

    def size(self):
        from ..common.choices import VariantCategory

        return self.filter(variant_category=VariantCategory.SIZE)