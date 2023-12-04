from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'all_posts_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'author', 'body']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('list')




