from ..forms.reviewform import ReviewsModelForm
from django.shortcuts import redirect
from ..models.review import Reviews
from django.contrib import messages


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
            messages.success(request, "accept your comment")
        else:
            messages.error(request, f"bad comment:{form.errors.as_text()}")
    return redirect(url)
