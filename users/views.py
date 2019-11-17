from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .forms import UserRegisterForm
from django.contrib.auth.models import User

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def main_page_view(request):
    return render(request, "index.html", {})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Konto zostało założone dla {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('/')


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
    paginator = Paginator(users_list, 10)
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
