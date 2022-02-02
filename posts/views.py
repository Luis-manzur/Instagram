#Django
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from django.views.generic.detail import DetailView

#Forms
from posts.forms import PostForm

#Models
from posts.models import Post

#Utilities
from datetime import datetime

class PostsListView(LoginRequiredMixin, ListView):

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/post_detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

class CreatePostView(LoginRequiredMixin, CreateView):
    
    template_name = 'posts/create_post.html'
    model = Post
    form_class = PostForm
    fields = ['title', 'photo']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.profile = self.request.user.profile
        form.save()
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('posts:feed')
