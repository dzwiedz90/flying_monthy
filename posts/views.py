from django.http import request
from django.shortcuts import render

# Create your views here.
from .models import Post
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class List(ListView):
    model = Post
    template_name = 'list.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'category', 'cover']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def post_view():
    pass
