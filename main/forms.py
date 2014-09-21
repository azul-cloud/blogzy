from django import forms
from django.forms import ModelForm

from main.models import Feedback

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Button, Fieldset, ButtonHolder, Field


class FeedbackForm(ModelForm):
    feedback = forms.CharField(widget = forms.Textarea())

    class Meta:
        model = Feedback

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'feedback-form'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('user', required=False, type="hidden"),
                Div('feedback'),
            ),
            ButtonHolder(
                Button('button', 'Send Feedback', css_class='btn-lg btn-primary', css_id='feedback-submit'), css_class="text-center"
            )
        )