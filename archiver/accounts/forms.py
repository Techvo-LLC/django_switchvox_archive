from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label = 'first name', max_length=50, required = True)
    last_name = forms.CharField(label = 'last name', max_length=50, required = True)
    email = forms.EmailField(label="email address", required=True)

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','password1','password2')