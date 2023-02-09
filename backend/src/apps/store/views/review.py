from ..forms.reviewform import ReviewsModelForm
from django.shortcuts import redirect
from django.http import HttpResponse
from ..models.review import Reviews


def add_review(request, product_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = ReviewsModelForm(request.POST)
        if form.is_valid():
            data = Reviews()
            data.desc = form.cleaned_data["desc"]
            data.rating = form.cleaned_data["rating"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.user = request.user
            data.product_id = product_id
            data.save()
        else:
            return HttpResponse("Error")

    return redirect(url, category_slug=data.product.category.slug, product_slug=data.product.slug)
