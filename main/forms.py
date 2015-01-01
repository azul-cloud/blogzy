from django import forms
from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Button, Fieldset, ButtonHolder, Field

from .models import Contact


class ContactForm(ModelForm):
    message = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = Contact
        fields = ['user', 'type', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'contact-form'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('user', required=False, type="hidden"),
                Div('type'),
                Div('message'),
            ),
            ButtonHolder(
                Button('button', 'Send Contact', 
                    css_class='btn-lg btn-primary',
                    css_id='contact-submit'), 
                css_class="text-center"
            )
        )