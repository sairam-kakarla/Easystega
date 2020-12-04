from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=["email","username","password1","password2"]
