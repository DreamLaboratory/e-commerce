from django.core.management import BaseCommand

from ..models.category import Category

class Command(BaseCommand):
    help='auto create product'


    def handle(self,*args,**kwargs):
        product_dict={'meva':'daxshat zur','keyim':'daxshat','mashina':'GM mashina olma','Compyuter':'macbook pro va windowslar'}

        for k,v in product_dict.items():
            Category.objects.create(
                name=k,
                description=v,
            )