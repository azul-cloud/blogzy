from django.test import TestCase
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.auth.models import User

from .models import Topic, PersonalBlog, Post, UserFavorite, \
    UserStreamBlog, BlogSubscription


class BlogTestSetup(TestCase):
    def setUp(self):
        self.prefix = "blog-"

        self.user = User.objects.create_user('blog_tester', 
            'tester@somewhere.com', 'testpassword')

        self.user2 = User.objects.create_user('blog_tester2', 
            'tester@somewhere.com', 'testpassword')

        self.topic = Topic.objects.create(title=u"Test Topic")

        self.blog = PersonalBlog.objects.create(title=u"test blog title", 
            owner_id=self.user.id, description="This is my test blog")

        self.post = Post.objects.create(author = self.user, blog=self.blog,
            image = '/', title=u"Test Post Title", body="<h1>This is my test post body</h1>", 
            active=True)

        self.user_favorite = UserFavorite.objects.create(user=self.user,
            post=self.post)

        self.user_stream_blog = UserStreamBlog.objects.create(user=self.user,
            blog=self.blog)

        self.blog_subscription = BlogSubscription.objects.create(user=self.user,
            blog=self.blog, sub_type="M")

    def login(self):
        '''
        used to check permissions on the user that SHOULD have access
        '''
        self.client.login(username=self.user.username, 
            password='testpassword')

    def login_second_user(self):
        '''
        used to check permissions on other logged in user
        '''
        self.client.login(username=self.user2.username, 
            password='testpassword')


class BlogModelTest(BlogTestSetup):

    def test_topic(self):
        # select topic and make sure slug was saved
        topic = Topic.objects.get(title=self.topic.title)
        self.assertNotEqual(topic.slug, None)

    def test_blog(self):
        blog = PersonalBlog.objects.get(title=self.blog.title)
        self.assertNotEqual(blog.slug, None)

    def test_post(self):
        post = Post.objects.get(title=self.post.title)
        self.assertNotEqual(post.slug, None)

    def test_user_favorite(self):
        user_favorite = UserFavorite.objects.get(user=self.user, post=self.post)

    def test_user_stream_blog(self):
        stream = UserStreamBlog.objects.get(user=self.user, blog=self.blog)

    def test_blog_subscription(self):
        blog_subscription = BlogSubscription.objects.get(user=self.user)


class BlogViewTest(BlogTestSetup):

    def test_create_blog(self):
        url = reverse(self.prefix + "create")
        response = self.client.get(url)

    def test_blog_home(self):
        url = reverse(self.prefix+"blog", kwargs={'blog':self.blog.slug})
        
        response = self.client.get(url)
        self.assertContains(response, self.blog.title)

    def test_blog_post(self):
        url = reverse(self.prefix+"post", kwargs={'blog':self.blog.slug,
            'post':self.post.slug})
        
        response = self.client.get(url)
        self.assertContains(response, self.post.title)

    def test_blog_topic(self):
        url = reverse(self.prefix+"topic", kwargs={'topic':self.topic.slug})
        
        response = self.client.get(url)
        self.assertContains(response, self.topic.title)

    def test_blog_dashboard(self):
        url = reverse(self.prefix + "dashboard", kwargs={'blog':self.blog.slug})

        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login_second_user()
        second_user_response = self.client.get(url)
        self.assertEqual(second_user_response.status_code, 404)

        self.login()
        response = self.client.get(url)
        self.assertContains(response, self.blog.title)

    def test_create_blog(self):
        url = reverse(self.prefix + "create")

        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_post_edit(self):
        url = reverse(self.prefix + "post-edit", kwargs={'pk':self.post.id})

        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login()
        response = self.client.get(url)
        self.assertContains(response, self.post.title)

    def test_blog_post_create(self):
        url = reverse(self.prefix + "post-create")

        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_explore(self):
        url = reverse(self.prefix + "explore")

        response = self.client.get(url)

    def test_topic(self):
        url = reverse(self.prefix + "topic", kwargs={'topic':self.topic.slug})

        response = self.client.get(url)

    def test_wave(self):
        url = reverse(self.prefix + "wave")

    def test_wave_add(self):
        url = reverse(self.prefix + "wave-add", kwargs={"pk":self.blog.id,
            "action":"add"})

        self.login()
        response = self.client.get(url)

    def test_wave_remove(self):
        url = reverse(self.prefix + "wave-remove", kwargs={"pk":self.blog.id,
            "action":"remove"})

        self.login()
        response = self.client.get(url)

    def test_favorites(self):
        url = reverse(self.prefix + "favorites")

        anon_response = self.client.get(url)
        self.assertEqual(anon_response.status_code, 302)

        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class BlogFormTest(BlogTestSetup):
    def test_create_blog(self):
        pass
        # self.client.login(username=self.user2.username, 
        #     password='testpassword')
        
        # url = reverse('blog-create')

        # post = {
        #     "title":"My Test Blog",
        #     "description":"<h1>BEST TEST BLOG EVER!</h1>",
        # }

        # response = self.client.post(url, post)

        # # make sure the response has the newly created post
        # self.assertEqual(response.status_code, 302)
        # self.assertContains(response, post['title'])

    def test_edit_blog(self):
        pass

    def test_create_post(self):
        pass

    def test_edit_post(self):
        pass
