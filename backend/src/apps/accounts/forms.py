from django import forms
from .models import MyUser
class RegisterForm(forms.ModelForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email'}) ,required=True)
    username=forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}))
    
    class Meta:
        model=MyUser
        fields=['first_name','last_name']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'form-control','placeholder':'first name'})
        self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'last name'})
        self.fields['first_name'].label='First name'
        self.fields['last_name'].label='Last name'

    
    
