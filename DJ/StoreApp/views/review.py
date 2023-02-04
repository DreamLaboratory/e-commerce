from django.shortcuts import redirect
from ..models.review import Review
from ..forms.review_form import ReviewForm

def add_review(request,product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method=='POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = Review()
            data.desc = form.cleaned_data.get('desc')
            data.rating = form.cleaned_data.get('rating')
            data.ip = request.META.get('REMOTE_ADDR')
            data.user = request.user
            data.product_id = product_id
            data.save()
        return redirect(url)
