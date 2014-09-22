from django import forms
from django.forms import ModelForm

from blog.models import PersonalBlog, Post, Topic

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, Fieldset, ButtonHolder, Field, Button


class BlogCreateForm(ModelForm):
    title = forms.CharField(help_text="What is the name of your blog?")
    description = forms.CharField(widget = forms.Textarea(),
                                  help_text="Give people an idea what your blog is all about")
    logo = forms.ImageField(required=False, help_text="Optional. Recommended square image.")

    class Meta:
        model = PersonalBlog
        exclude = ['owner', 'slug']

    def __init__(self, *args, **kwargs):
        super(BlogCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                '<h1>Create Your Travel Blog</h1>',
                Div('title', css_class="col-sm-6", css_id="title"),
                Div('logo', css_class="col-sm-6", css_id="logo"),
                Div('description', css_class="col-sm-12", css_id="description")
            ),
            ButtonHolder(
                Submit('submit', 'Create Blog', css_class='btn-lg'), css_class="text-center"
            )
        )


class BlogPostCreateForm(ModelForm):
    place = forms.CharField(required=False, help_text="Allow post to show on maps, and for people to find your post when searching by place")
    headline = forms.CharField(required=False, help_text="100 character headline of your post. Will appear on map popup and other places")
    # topic = forms.MultipleChoiceField(required=False)

    class Meta:
        model = Post
        exclude = ['author', 'blog']

    def __init__(self, *args, **kwargs):
        super(BlogPostCreateForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('views', type="hidden"),
                Field('place_id', type="hidden"),
                Div('title', css_class="col-sm-5 col-xs-6"),
                # Div('topic', css_class="col-sm-3 col-xs-6"),
                Div(
                    Field('place', id="place-search"),
                    css_class="col-sm-5 col-xs-6",
                    # todo: hidden-xs. need to modify crispyforms
                    ),
                Div('active', css_class="col-sm-2 hidden-xs"),
                Div('headline', css_class="col-xs-12 col-sm-offset-1 col-sm-10"),
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
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('views', type="hidden"),
                Field('place_id', type="hidden"),
                Div('title', css_class="col-sm-5 col-xs-6"),
                # Div('topic', css_class="col-sm-5 col-xs-6"),
                Div(
                    Field('place', id="place-search"),
                    css_class="col-sm-5 col-xs-6",
                    # todo: hidden-xs. need to modify crispyforms
                    ),
                Div('active', css_class="col-sm-2 hidden-xs"),
                Div('headline', css_class="col-xs-12 col-sm-offset-1 col-sm-10"),
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
    twitter = forms.CharField(required=False, help_text="show twitter feed, and allow people to interact with you on twitter")
    twitter_widget_id = forms.CharField(required=False, help_text="required to show a timeline widget for your twitter account. " + \
                                                  "<span class='glyphicon glyphicon-question-sign'></span>")
    instagram = forms.CharField(required=False, help_text="show instagram feed on your blog page (coming soon)")
    disqus = forms.CharField(required=False, help_text="allow comments at the bottom of your blog posts")

    class Meta:
        model = PersonalBlog

    def __init__(self, *args, **kwargs):
        super(BlogEditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                '<h2 class="text-center">Edit data about your blog</h2>',
                Field('owner', type="hidden"),
                Field('title', type="hidden"),
                Div('description', css_class="col-md-12"),
                Div('twitter', css_class="col-md-6"),
                Div('twitter_widget_id', css_class="col-md-6"),
                Div('instagram', css_class="col-md-6"),
                Div('disqus', css_class="col-md-6"),
                Div('logo', css_class="col-md-12"),
            ),
            ButtonHolder(
                Submit('submit', 'Update Info', css_class='btn-lg'),
                css_class="text-center"
            ),

        )