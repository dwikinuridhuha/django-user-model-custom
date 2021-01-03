from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserCustom

class UserCustomCreation(UserCreationForm):
    class Meta:
        model=UserCustom
        fields=('username','email','password')

class UserCustomChange(UserChangeForm):
    class Meta:
        model=UserCustom
        fields=('username','email','password')