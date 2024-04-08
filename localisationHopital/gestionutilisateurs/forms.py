from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['first_name'].label = ''
        self.fields['first_name'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'First Name'
        })
        
        self.fields['last_name'].label = ''
        self.fields['last_name'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Last Name'
        })
        
        self.fields['email'].label = ''
        self.fields['email'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Email'
        })
        
        self.fields['username'].label = ''
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Username'
        })
        
        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter Password'
        })
        
        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirmation Password'
        })
        
        # self.fields['password2'].widget.attrs['class']='form-control'
