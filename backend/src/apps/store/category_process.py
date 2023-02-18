from .models.category import Category


def categories_all(request):
    try:
        return dict(catigories=Category.objects.all())
    except:
        return dict(catigories=None)
