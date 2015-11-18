from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView

from blog.models import Post
from .forms import ProfileUpdateForm


class HomeView(TemplateView):
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.map_eligible()
        return context


class StartView(ListView):
    template_name = "main/start.html"
    model = Post


class ProfileUpdateView(UpdateView):
    template_name = "main/profile_update.html"
    form_class = ProfileUpdateForm

    def get_object(self, **kwargs):
        return get_user_model().objects.get(id=self.request.user.id)

    def get_success_url(self):
        return reverse('main-profile-update')

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['page'] = 'profile'
        return context

    def form_valid(self, form):
        self.object = form.save()

        context = self.get_context_data(form=form)
        context["success"] = True
        return self.render_to_response(context)


class RobotTemplateView(TemplateView):
    template_name = "main/robots.txt"
