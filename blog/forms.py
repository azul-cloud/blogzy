from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

from .models import Post


class PostCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div(
                    Div('title', css_class="col s12 m4"),
                    Div('headline', css_class="col s12 m8"),
                    css_class="row"
                ),
                Div(
                    Div('image', css_class="col m6 s12"),
                    Div('image_description', css_class="col m6 s12"),
                    css_class="row"
                ),
                Div(
                    Div('public', css_class="col m6 s12"),
                    Div('topics', css_class="col m6 s12"),
                    css_class="row"
                ),
                Div(
                    Div('body', css_class="col s12"),
                    css_class="row"
                )
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn')
            )
        )

    class Meta:
        model = Post
        exclude = ['author', 'blog', 'lat', 'lng', 'place',
            'place_id']
