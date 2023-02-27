from django import forms
from .models.review import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rate', 'description')
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "rate": forms.NumberInput(attrs={"class": "form-control"}),
        }
        



