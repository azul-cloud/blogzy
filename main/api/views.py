from django.template import Context

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from crispy_forms.templatetags.crispy_forms_tags import CrispyFormNode

from blog.models import Post
from blog.forms import PostEditForm, EditPostHelper
from ..models import Feedback
from .serializers import FeedbackSerializer


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


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
        helper = EditPostHelper()

        # we need to use crispy forms to add the form + button + materialize render
        context = Context({
            "post_edit_form": form,
            "helper": helper
        })

        html = CrispyFormNode("post_edit_form", None).render(context)

        return Response(data={'html':html})
