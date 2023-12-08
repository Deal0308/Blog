from typing import Any
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView,)
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post, Status
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)
# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publish_status = Status.objects.get(name='published')
        context['post_list'] = Post.objects.filter(
            status=publish_status
        ).order_by('created_on').reverse()        
        
        return context
    
class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name='draft')
        context['post_list'] = Post.objects.filter(
            status=draft_status
        ).order_by('created_on').reverse()        
        
        return context
    

class ArchiveListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'posts/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publish_status = Status.objects.get(name='published')
        context['post_list'] = Post.objects.filter(
            status=publish_status
        ).filter(author=self.request.user
        
        ).order_by('created_on').reverse()        
        
        return context

    


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/new.html'
    fields = ['title', 'subtitle', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']

    def test_func(self):     
        post = self.get_object()
        return post.author == self.request.user
    
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('list')

    def test_func(self):     
        post = self.get_object()
        return post.author == self.request.user




