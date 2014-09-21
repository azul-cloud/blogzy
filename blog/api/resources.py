from django.core.exceptions import ValidationError

from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie.authentication import Authentication

from blog.models import Post, PersonalBlog, Topic, UserFavorite
from main.api.resources import UserResource


class TopicResource(ModelResource):
    '''
    list of all topics
    '''

    class Meta:
        queryset = Topic.objects.all()
        filtering = {
            'slug': ALL,
        }


class PostResource(ModelResource):
    '''
    get and create individual blog posts
    '''
    author = fields.ForeignKey(UserResource, 'author', full=True)
    blog = fields.ForeignKey('blog.api.resources.BlogResourceEmpty', 'blog', full=True)
    topic = fields.ForeignKey(TopicResource, 'topic', null=True)

    get_absolute_url = fields.CharField(attribute='get_absolute_url', readonly=True)
    get_image_url = fields.CharField(attribute='get_image_url', readonly=True)

    class Meta:
        ordering = ['create_date']
        queryset = Post.objects.all()
        allowed_methods = ['get', 'post', 'delete']
        filtering = {
            'topic': ALL_WITH_RELATIONS,
        }


class PostResourceEmpty(PostResource):
    '''
    show post information without showing full relations and hide body
    '''
    author = fields.ForeignKey(UserResource, 'author')
    blog = fields.ForeignKey('blog.api.resources.BlogResource', 'blog')

    class Meta:
        excludes = ['body']



class BlogResource(ModelResource):
    '''
    get and create personal blog objects
    '''
    owner = fields.ForeignKey(UserResource, 'owner', full=True)
    posts = fields.ToManyField(PostResource, 'post_set', related_name='post', full=True)

    total_subscription_count = fields.IntegerField(attribute='total_subscription_count', readonly=True)
    google_id = fields.CharField(attribute='google_id', readonly=True)
    get_absolute_url = fields.CharField(attribute='get_absolute_url', readonly=True)

    class Meta:
        queryset = PersonalBlog.objects.all()
        filtering = {
            'slug': ALL,
            'owner': ALL_WITH_RELATIONS
        }

    def hydrate_owner(self, bundle):
        # build the current user to save as the blog owner
        bundle.data['owner'] = bundle.request.user
        return bundle


class BlogResourceEmpty(BlogResource):
    '''
    Need to have a blog resource that doesn't have posts full, so that we can link
    to it from the postresource
    '''
    posts = fields.ToManyField(PostResource, 'post_set', related_name='post')


class UserFavoriteResource(ModelResource):
    '''
    manage post favorites by a user. Users can use a favorites list
    to easily view posts that they have liked or deemed important.
    '''
    user = fields.ForeignKey(UserResource, 'user')
    post = fields.ForeignKey('blog.api.resources.PostResource', 'post', full=True)
    allowed_methods = ['get', 'post']

    class Meta:
        queryset = UserFavorite.objects.all()
        filtering = {
            'user':ALL_WITH_RELATIONS
        }
        authentication = Authentication()
        authorization = Authorization()

    def hydrate_user(self, bundle):
        # build the current user to save for the favorite instance
        bundle.data['user'] = bundle.request.user
        return bundle

    def get_object_list(self, request):
        # filter results to the current user
        return super(UserFavoriteResource, self).get_object_list(request)\
            .filter(user=request.user)