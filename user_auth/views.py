from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages


def custom_login(request):
    context = {}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])

            return HttpResponseRedirect(reverse('user_auth_profile'))
        else:
            print("Incorrect username or password")
            messages.warning(request, 'Incorrect username or password')
            return render(request, "account/login.html")
    else:
        print("Somthisng wronf")
        return render(request, "account/login.html", context)



@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, "account/profile.html", context)


def user_landing(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('user_auth_profile'))
    else:
        return HttpResponseRedirect(reverse('account_login'))