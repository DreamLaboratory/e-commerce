from django import forms
from .models import MyUser
class RegisterForm(forms.ModelForm):

    password=forms.CharField(
                            widget=forms.PasswordInput(
                                                        attrs={
                                                            'class':'form-control',
                                                            'place-holder':'Enter password'
                                                               }
                                                      ),
                            max_length=50,
                            )
    confirm_password=forms.CharField(

                                widget=forms.PasswordInput(
                                                            attrs={
                                                                'class':'form-control',
                                                                'place-holder':'again Enter password'
                                                                }
                                                            ),
                                max_length=50,
                                    )
    
    class Meta:
        model=MyUser
        fields=['first_name','last_name','email','password','confirm_password']
 

    def clean(self):
        clean_data=super(RegisterForm,self).clean
        password=clean_data.get('password')
        confirm_password=clean_data.get('confirm_password')
        
        if password != confirm_password:
            return forms.ValidationError("password and confirm password aren't same between them")
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm,self).__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
        
    
    
