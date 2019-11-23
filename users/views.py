from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from posts.models import Post
from .forms import UserRegisterForm
from django.conf import settings


def main_page_view(request):
    object_list = Post.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, settings.PAGINATION_SIZE)
    try:
        memes = paginator.page(page)
    except PageNotAnInteger:
        memes = paginator.page(1)
    except EmptyPage:
        memes = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'memes': memes})


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
    messages.success(request, f"Wylogowano użytkownika {username}")
    return redirect('/')


@login_required(login_url='/accounts/login/')
def users_list(request):
    users_list = User.objects.all()
    data = request.POST
    search_by = data.get('search_by')
    search_value = data.get('search')
    if search_by == 'user':
        all = []
        for user in users_list:
            if search_value.lower() in str(user).lower():
                all.append(user)
        users_list = all

    elif search_by == 'role':
        if search_value.lower() in "administrator":
            users_list = users_list.filter(is_superuser=True)
        elif search_value.lower() in "moderator":
            users_list = users_list.filter(is_staff=True, is_superuser=False)
        elif search_value.lower() in "użytkownik" or search_value.lower() in "uzytkownik":
            users_list = users_list.filter(is_staff=False, is_superuser=False)

    page = request.GET.get('page', 1)
    paginator = Paginator(users_list, settings.PAGINATION_SIZE)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'users_list.html', {'users': users})


def change_user_status(request, pk):
    if request.method == "POST":
        data = request.POST
        user = User.objects.get(pk=pk)
        role = data.get('new_role')
        if role == 'administrator':
            user.is_superuser = True
        elif role == 'moderator':
            user.is_staff = True
        elif role == 'uzytkownik':
            user.is_superuser = False
            user.is_staff = False
        user.save()
        return redirect("/users_list")
    # messages.success(request, f"Użytkownik {username} został wylogowany.")
    # return redirect('/')


@login_required()
def profile(request):
    object_list = Post.objects.filter(author=request.user.id)
    page = request.GET.get('page', 1)
    paginator = Paginator(object_list, settings.PAGINATION_SIZE)
    try:
        memes = paginator.page(page)
    except PageNotAnInteger:
        memes = paginator.page(1)
    except EmptyPage:
        memes = paginator.page(paginator.num_pages)

    return render(request, "profile.html", {'memes': memes})
