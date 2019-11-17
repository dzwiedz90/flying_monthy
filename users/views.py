from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
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
    username = request.user.username
    auth.logout(request)
    return redirect('/')


def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

# request_data.get('new_role') -> 'Użytkownik'
def change_user_status(request, pk):

    if request.method == "POST":
        data = request.POST
        user = User.objects.get(pk=pk)
        role = data.get('new_role')
        # import ipdb;
        # ipdb.set_trace()
        # polecenia do użycia w konsoli aby sprawdzić co się dzieje pod do import ipdb
        # c -continue
        # n - new line
        # s - step (wejdz do środka funkcji)
        if role == 'administrator':
            user.is_superuser = True
        elif role == 'moderator':
            user.is_staff = True
        elif role == 'uzytkownik':
            user.is_superuser = False
            user.is_staff = False
        user.save()
        return redirect("/users_list")
    messages.success(request, f"Użytkownik {username} został wylogowany.")
    return redirect('/')


@login_required()
def profile(request):
    return render(request, 'profile.html')