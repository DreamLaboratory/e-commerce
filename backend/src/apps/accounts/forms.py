from .models import User, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password Again'}))

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'User Name'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))

    class Meta:
        model = User
        fields = ('username', 'phone_number',
                  'email', 'password1', 'password2')
                  

class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"




class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'User Name'}))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    phone_number = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone Number'}))
    class Meta:
        model = User
        fields = ('username', 'phone_number','email')
        
