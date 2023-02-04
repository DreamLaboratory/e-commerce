from django import forms

from ..models import Account
from django.contrib.auth import authenticate, password_validation
from django.core.exceptions import ValidationError


# UserCreationForm is a built-in form in Django
class ResetPasswordForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
        max_length=100,
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        ),
        max_length=100,
    )

    class Meta:
        model = Account
        fields = ("password", "confirm_password")

    def clean(self):
        print("clean method ishladi")
        cleaned_data = super(ResetPasswordForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")

    def _post_clean(self):
        print("post_clean method ishladi")
        super()._post_clean()
        # Validate the password after self.instance is updated with form data
        # by super().
        password = self.cleaned_data.get("password")
        if password:
            try:
                password_validation.validate_password(password, self.instance)
            except ValidationError as error:
                self.add_error("password", error)

    def __init__(self, *args, **kwargs):
        super(ResetPasswordForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
        # self.fields["password"].widget.attrs["placeholder"] = "Password"
        # self.fields["confirm_password"].widget.attrs["placeholder"] = "Confirm_password"