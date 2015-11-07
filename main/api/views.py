from rest_framework.views import APIView
from rest_framework.response import Response

from blog.models import Post
from blog.forms import PostEditForm


class EditPostFormHtml(APIView):
    """
    This is an endpoint to return form HTML code. We generate forms
    through AJAX but want the server to render the HTML code to
    output
    """
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        instance = Post.objects.get(id=pk)
        form = PostEditForm(instance=instance)

        return Response(data={'html':form.as_p()})
