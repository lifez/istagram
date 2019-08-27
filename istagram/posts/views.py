from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import Post

class CreatePostView(CreateView):
    model = Post
    fields = ['text', 'image']
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ListPostView(ListView):
    queryset = Post.objects.all()