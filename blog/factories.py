from factory.django import DjangoModelFactory

from django.contrib.auth import get_user_model

from .models import Topic, PersonalBlog, Post, UserFavorite, UserStreamBlog,\
                    BlogSubscription, BlogSubscriptionLog

User = get_user_model()


# class TopicFactory(DjangoModelFactory):
#     # this will get passed in the title
#     class Meta:
#         model = Topic

    # title = "Test Topic"


# class PersonalBlogFactory(DjangoModelFactory):
    
#     class Meta:
#         model = PersonalBlog

#     Description = "Test Blog"


# class PostFactory(DjangoModelFactory):
#     class Meta:
#         model = Post

#     blog   = PersonalBlogFactory.create(),
#     image  = '/', 
#     title  = u"Test Post Title" 
#     body   = "<h1>This is my test post body</h1>", 
#     active = True


# class UserFavoriteFactory(DjangoModelFactory):
#     class Meta:
#         model = UserFavorite


# class UserStreamBlogFactory(DjangoModelFactory):
#     class Meta:
#         model = UserStreamBlog


# class BlogSubscriptionFactory(DjangoModelFactory):
#     class Meta:
#         model = BlogSubscription


# class BlogSubscriptionLogFactory(DjangoModelFactory):
#     class Meta:
#         model = BlogSubscriptionLog



