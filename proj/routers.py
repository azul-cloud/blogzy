from rest_framework.routers import DefaultRouter

from blog.api import BlogViewSet, PostViewSet

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('posts', PostViewSet)
