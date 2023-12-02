from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import PasswordChangeDoneView
from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import Post


# Create your views here.
class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class PasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
    success_url = reverse_lazy('login')

class PostlistView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'
    ordering = ['-created_on']

class PostDetailView(ListView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'all_posts_list'
    ordering = ['-created_on']

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'subtitle', 'author', 'body']
    success_url = reverse_lazy('home')

class PostUpdateView(CreateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'subtitle', 'body']
    success_url = reverse_lazy('home')  





