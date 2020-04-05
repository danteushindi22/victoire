from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')

    class Meta():
        model = User
        fields = ('username', 'email')
