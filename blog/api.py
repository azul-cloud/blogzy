from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import PersonalBlog, Post
from .serializers import BlogSerializer, PostSerializer


class BlogViewSet(ReadOnlyModelViewSet):
    queryset = PersonalBlog.objects.all()
    serializer_class = BlogSerializer


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_fields = ('blog', )
