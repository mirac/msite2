from django import forms
from models import User


class UserForm(forms.Model):
    class Meta:
        model = User
        widgets = {
            'password': forms.PasswordInput(),
        }
