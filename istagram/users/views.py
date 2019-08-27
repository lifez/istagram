from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import User
from posts.models import Post


class ProfileDetailView(DetailView):
    model = User

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super(ProfileDetailView, self).get_context_data(**kwargs)

        # context['posts'] = Post.objects.filter(user=request.user)
        context["name"] = "Airmee"

        return context


