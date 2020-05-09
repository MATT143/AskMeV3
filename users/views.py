from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from task.models import MasterTasks


# Create your views here.

def home(request):
    return render(request,'users/home.html')

def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f'Successfuly Created Account! Please log in.')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})


@login_required
def profile(request):
    category=request.user.profile.category
    query=MasterTasks.objects.filter(category=category,isOccupied=False).order_by('-creation_date')
    return render(request,'users/profile.html',{'data':query})


@login_required
def UpdateSettings(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        Q = Profile.objects.filter(user=request.user)
        u_role = Q[0].user_role
        #request.FILES is for image data

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Profile Updated Succesfully!!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        Q = Profile.objects.filter(user=request.user)
        u_role=Q[0].user_role


    context={'u_form':u_form,'p_form':p_form,'u_role':u_role}
    return render(request,'users/updateSettings.html',context=context)








