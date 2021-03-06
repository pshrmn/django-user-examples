from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name')


class UserChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
