from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
    ordering = ['-created_on']

class BlogDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'all_posts_list'
    ordering = ['-created_on']

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'subtitle', 'author', 'body']
    success_url = reverse_lazy('home')
