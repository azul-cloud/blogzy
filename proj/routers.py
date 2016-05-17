from rest_framework.routers import DefaultRouter

from blog.api.views import BlogViewSet, PostViewSet
from main.api.views import FeedbackViewSet

router = DefaultRouter()

router.register('blogs', BlogViewSet)
router.register('posts', PostViewSet)
router.register('feedback', FeedbackViewSet)
