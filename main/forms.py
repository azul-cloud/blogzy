from collections import OrderedDict

from django import forms
from django.contrib.auth import get_user_model

from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div



class CustomSignupForm(SignupForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    base_fields = ['email', 'first_name', 'last_name', 'password1',
        'password2']

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'password1',
            'password2']

CustomSignupForm.base_fields = OrderedDict(
        (k, CustomSignupForm.base_fields[k])
        for k in ['email', 'first_name', 'last_name', 'password1',
            'password2', 'username']
)


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '<h2>Edit Your Profile</h2>',
                Div(
                    Div('first_name', css_class="col s12 m6"),
                    Div('last_name', css_class="col s12 m6"),
                    css_class="row"
                ),
                Div(
                    Div('image', css_class="col s12"),
                    css_class="row"
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Save', css_class='btn right hover-right')
            )
        )

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name",  "image"]
        # required = ["first_name"]
