from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


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




    # if request.method == "POST":
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['laast_name']
    #     username = request.POST['username']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     email = request.POST['email']
    #
    #     user = User.objects.create_user(username=username, password=password1, email=email,
    #                                     first_name=first_name, last_name=last_name)
    #     user.save();
    #     print("User created")
    #     return redirect('/')
    #
    # else:
    #     return render(request, 'registration/register.html')
