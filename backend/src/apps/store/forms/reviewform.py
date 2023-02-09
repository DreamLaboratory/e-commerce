from django import forms
from ..models.review import Reviews


class ReviewsModelForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ["desc", "rating"]
        widgets = {
            "desc": forms.Textarea(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
        }
