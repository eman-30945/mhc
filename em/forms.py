from dataclasses import fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *
from django import forms

class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']

 
 