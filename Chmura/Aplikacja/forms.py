from django.forms import ModelForm 
from .models import Zamowienie
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class ZamowienieForm(ModelForm):
    class Meta:
        model = Zamowienie
        fields = '__all__'

class StworzUseraForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']