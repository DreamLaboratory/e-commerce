from .models.category import Category

def categories_all(request):
    
    return dict(catigories=Category.objects.all())


