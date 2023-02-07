from django import forms

from ..models.review import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["desc", "rating"]
        widgets = {
            "desc": forms.Textarea(attrs={"class": "form-control"}),
            "rating": forms.NumberInput(attrs={"class": "form-control"}),
        }


# def validate_desc(value):
#     # TODO move to forms.py
#     # list of bad words
#     bad_words = ["yomon"]
#     # check if bad words in review description
#     if any(word in value for word in bad_words):
#         raise forms.ValidationError("Bad words in review description")
