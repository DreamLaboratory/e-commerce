from django.shortcuts import redirect
from django.contrib import messages
from ..forms.review_form import ReviewForm
from ..models.review import Review


# add review
def add_review(request, product_id):
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            # altirnative way = new_form = form.save(commit=False)
            data = Review()
            data.desc = form.cleaned_data["desc"]
            data.rating = form.cleaned_data["rating"]
            data.ip = request.META.get("REMOTE_ADDR")
            data.user = request.user
            data.product_id = product_id
            data.save()
            messages.success(request, "Successfully added review")
        messages.warning(request, form.errors)
    return redirect(url)
