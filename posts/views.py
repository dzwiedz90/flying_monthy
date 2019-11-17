from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm


class List(ListView):
    model = Post
    template_name = 'list.html'


class CreateMemeView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')
