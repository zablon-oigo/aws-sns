from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=CustomUser
        fields=("email",)
class SignUpForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('email','password1','password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)