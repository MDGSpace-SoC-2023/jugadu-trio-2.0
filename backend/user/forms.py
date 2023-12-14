from django import forms
from .models import CommonUser


class SignupForm(forms.ModelForm):
    class Meta:
        model = CommonUser
        fields = ['email', 'password']