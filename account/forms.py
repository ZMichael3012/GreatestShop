from django import forms
from .models import Client


class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].empty_value = 'GreatestPassword'

    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'email',
            'password'
        ]
        widgets = {
            'password': forms.PasswordInput()
        }
