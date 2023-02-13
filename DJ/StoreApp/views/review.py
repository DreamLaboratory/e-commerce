import logging
from django.contrib import messages
from django.shortcuts import redirect
from ..models.review import Review
from ..forms.review_form import ReviewForm



def add_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            print(request.POST)
            if form.is_valid():
                data = Review()
                data.desc = form.cleaned_data.get('desc')
                data.rating = form.cleaned_data.get('rating')
                data.ip = request.META.get('REMOTE_ADDR')
                data.user = request.user
                data.product_id = product_id
                data.save()
                messages.success('Sizning fikringiz qabul qilindi')
                return redirect(url)
                print('salom')
            messages.error(request,f"this comment in bad words!")
    except Exception as e:
        return redirect(url)
