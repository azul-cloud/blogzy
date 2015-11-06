from django import forms
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm



class CustomSignupForm(SignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1',
            'password2']
