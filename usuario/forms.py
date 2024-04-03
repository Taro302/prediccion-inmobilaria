from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']



#Autentication Form
"""
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("usernme", "password",)
        
class AddUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email' , 'name', 'role', 'password',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'password': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
        }

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email' , 'name', 'role',)
        widgets = {
            'email': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'name': forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'role': forms.Select(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }        
"""