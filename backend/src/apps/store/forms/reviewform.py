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

    def clean_desc(self):

        desc = self.cleaned_data["desc"]
        bad_word = ["yoman"]
        if desc in bad_word:
            raise forms.ValidationError("Bad words in review descriptions")
        return desc
