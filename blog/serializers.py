from rest_framework.serializers import ModelSerializer

from .models import PersonalBlog, Post

class BlogSerializer(ModelSerializer):
    class Meta:
        model = PersonalBlog


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
