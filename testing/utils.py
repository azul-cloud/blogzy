
class AccessMixin(object):
    """ This mixin is to be used in tests when they require some sort of acccess
        tests
    """
    def login_required(self, url, text=None):
        # test if login is required
        anon_response = self.app.get(url)
        assert anon_response.status_code == 302

        response = self.app.get(url, user=self.user)
        assert response.status_code == 200

        if text:
            assert text in response

    def blog_admin_access(self, url, text=None):
        """ test blog admin pages such as editing a blog post or
            creating a new post in a blog
        """
        anon_response = self.app.get(url)
        assert anon_response.status_code == 302

        user_response = self.app.get(url, user=self.user)
        assert user_response.status_code == 302

        blog_admin_response = self.app.get(url, user=self.blog_user)
        assert blog_admin_response.status_code == 200

        if text:
            assert text in blog_admin_response