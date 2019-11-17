from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegisterForm
from posts.models import Post


# Create your views here.

def main_page_view(request):
    object_list = Post.objects.all()
    return render(request, "index.html", {'object_list': object_list})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Konto zostało założone dla {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')
