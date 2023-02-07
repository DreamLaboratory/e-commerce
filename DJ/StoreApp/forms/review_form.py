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

    def clean(self):
        bad_words = ['iflos', 'tentak', 'ahmoq']
        cleaned_data = super(ReviewForm, self).clean()
        desc = cleaned_data.get("desc")

        for bad in bad_words:
            if bad in desc:
                print('sux sdksdknsd')
                raise forms.ValidationError("bu suzni yozish mumkin emas!")

    # def __init__(self, *args, **kwargs):
    #     super(ReviewForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs["class"] = "form-control"
