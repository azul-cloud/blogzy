from django.forms import ModelForm

from .models import Post


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author', 'blog', 'lat', 'lng', 'place',
            'place_id']
