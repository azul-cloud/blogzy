from django import forms
from django.forms import ModelForm

from blog.models import PersonalBlog, Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button



class BlogPostCreateForm(ModelForm):
    place = forms.CharField(required=False, help_text="Allow post to show on maps, and for people to find your post when searching by place")
    headline = forms.CharField(required=False, help_text="100 character headline of your post. Will appear on map popup and other places")
    active = forms.BooleanField(required=False, help_text="Your post will not show up in explore, wave, or on your blog until you mark it active")
    # topic = forms.ModelMultipleChoiceField(required=False, queryset=Topic.objects.all())

    class Meta:
        model = Post
        exclude = ['author', 'blog']

    def __init__(self, *args, **kwargs):
        super(BlogPostCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'blog-post-create-form'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('place_id', type="hidden"),
                Div('title', css_class="col-sm-5 col-xs-6"),
                # Div('topic', css_class="col-sm-3 col-xs-6"),
                Div(
                    Field('place', id="place-search"),
                    css_class="col-sm-5 col-xs-6",
                    # todo: hidden-xs. need to modify crispyforms
                    ),
                Div('active', css_class="col-sm-2 hidden-xs"),
                Div('headline', css_class="col-xs-8 col-sm-6"),
                Div('image', css_class="col-sm-3"),
                Div('image_description', css_class="col-sm-3"),
                Div('body', css_class="col-xs-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Save Blog Post', css_class='btn-lg'),
                css_class="text-center"
            ),
        )


class BlogPostEditForm(BlogPostCreateForm):
    def __init__(self, *args, **kwargs):
        # add delete button to layout for the edit form
        super(BlogPostEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'blog-post-edit-form'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Div('title', css_class="col-sm-5 col-xs-6"),
                Field('place_id', type="hidden"),
                # Div('topic', css_class="col-sm-5 col-xs-6"),
                Div(
                    Field('place', id="place-search"),
                    css_class="col-sm-5 col-xs-6",
                    # todo: hidden-xs. need to modify crispyforms
                    ),
                Div('active', css_class="col-sm-2 hidden-xs"),
                Div('headline', css_class="col-xs-6"),
                Div('image', css_class="col-xs-4 col-sm-3"),
                Div('image_description', css_class="col-sm-3"),
                Div('body', css_class="col-xs-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Save Blog Post', css_class='btn-lg'),
                Button('button', 'Delete Post', css_class='btn-lg btn-danger'),
                css_class="text-center",
            ),
        )


class BlogEditForm(ModelForm):
    description = forms.CharField(widget = forms.Textarea())
    twitter = forms.CharField(required=False, 
        help_text="Show twitter feed, and allow people to interact with you on twitter")
    twitter_widget_id = forms.CharField(required=False, 
        help_text="Required to show a timeline widget for your twitter account. "\
        "For more information see <a href='https://twitter.com/settings/widgets'>Twitter Widget</a>")
    instagram = forms.CharField(required=False, 
        help_text="show instagram feed on your blog page",
        widget=forms.TextInput(attrs={
            'placeholder': 'Coming soon',
            'disabled': True,
        }))

    class Meta:
        model = PersonalBlog
        exclude = ['owner', 'title']

    def __init__(self, *args, **kwargs):
        super(BlogEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'blog-edit-form'
        self.helper.layout = Layout(
            Fieldset(
                '<h2 class="text-center">Edit data about your blog</h2>',
                Div('description', css_class="col-md-12"),
                Div('twitter', css_class="col-md-6"),
                Div('twitter_widget_id', css_class="col-md-6"),
                Div('instagram', css_class="col-md-6"),
            ),
            ButtonHolder(
                Submit('submit', 'Update Info', css_class='btn-lg'),
                css_class="text-center"
            ),
        )

