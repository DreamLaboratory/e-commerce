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

    def clean_description(self):
        desc = self.cleaned_data["desc"]
        print(desc)
        bad_words = ['iflos', 'tentak', 'ahmoq','bad']
        if any(word in desc for word in bad_words):
            raise forms.ValidationError("Bad words validate!")
        return desc

