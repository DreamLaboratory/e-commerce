from django.shortcuts import redirect

from ..forms.review_form import ReviewForm
from ..models.product import Product
from ..models.review import Review


# add review
def add_review(request, product_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # altirnative way = new_form = form.save(commit=False)
            form.save(commit=False)
            data = form.instance
            # print(111, data, 222, form.cleaned_data)
            data.desc = form.cleaned_data["desc"]
            data.rating = form.cleaned_data["rating"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.user = request.user
            data.product = Product.objects.get(id=product_id)
            data.save()
    return redirect(url)
