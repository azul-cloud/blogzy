from django import forms
from django.forms import ModelForm

from .models import PersonalBlog, Topic, BlogSubscription

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


class BlogCreateForm(ModelForm):
    title = forms.CharField(help_text="What is the name of your blog? This is the name of your blog, <b><u>not</u></b> an individual post.")
    description = forms.CharField(widget = forms.Textarea(),
                                  help_text="Give people an idea what your blog is all about")

    class Meta:
        model = PersonalBlog
        exclude = ['owner', 'slug']

    def __init__(self, *args, **kwargs):
        super(BlogCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'blog-create-form'
        self.helper.layout = Layout(
            Fieldset(
                '<h1>Create Your Travel Blog</h1>',
                Div('title', css_id="title"),
                Div('description', css_id="description")
            ),
            ButtonHolder(
                Submit('submit', 'Create Blog', css_class='btn-lg'), css_class="text-center"
            )
        )


class CreateBlogSubscriptionForm(ModelForm):
    class Meta:
        model = BlogSubscription
        exclude = ['blog']

    def __init__(self, *args, **kwargs):
        super(CreateBlogSubscriptionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'blog-subscription-form'
        self.helper.layout = Layout(
            Fieldset(
                '<h3 class="skinny text-center">Stay updated with the newsletter</h3>',
                Div('email', css_class="col-sm-12"),
                Div('frequency', css_class="col-sm-12"),
                Div(
                    Submit('submit', 'Join', css_class="btn-block"),
                        css_class="text-center col-sm-12"
                )
            ),

        )



