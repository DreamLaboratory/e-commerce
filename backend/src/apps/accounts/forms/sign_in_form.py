from django import forms
from ..models import Account


class SignInForm(forms.Form):
    confirm_password = forms.CharField(widget=forms.CharField(attrs={
        'placeholder': 'Email',
    }), max_length=30)
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
    }), max_length=30)


    class Meta:
        model = Account
        fields = ('email', 'password')


    # def __init__(self, *args, **kwargs):
    #     super(SignInForm, self).__init__(*args, **kwargs)
    #     for field in self.fields:
    #         self.fields[field].widget.attrs['class'] = 'form-control'
