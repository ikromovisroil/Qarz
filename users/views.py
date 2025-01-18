from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth
from django.contrib import messages
from .forms import *

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = Userloginform(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password,)
            if user and user.is_active:
                auth.login(request, user)
                if user.is_staff:
                    return redirect(reverse('profil'))
                else:
                    return redirect(reverse('login'))
        else:
            messages.error(request, "Iltimos, to'g'ri foydalanuvchi nomi va parolni kiriting.")
    else:
        form = Userloginform()
    context = {'form':form,}
    return render(request, 'registration/login.html',context)


def register(request):
    if request.method == 'POST':
        form = Userregisterform(request.POST)
        if form.is_valid():
            user = form.save(request)
            user.admin = True
            user.save()
            return redirect(reverse('login'))
        messages.error(request, "Muvaffaqiyatsiz ro'yxatdan o'tish. Yaroqsiz maʼlumot.")
    else:
        form = Userregisterform()
    context = { 'form': form }
    return render(request, 'registration/register.html', context)


def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))
