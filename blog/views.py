
from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm,LoginForm
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from . models import Post
from . forms import PostForm,DashBoardChange
# Create your views here.
def home(request):
    datas = Post.objects.all()
    return render(request,'blog/home.html',{'datas':datas})

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm()
            messages.success(request,'Account created successfully.')
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if  not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/profile/')
        else:
            form = LoginForm()
        return render(request,'blog/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        datas = Post.objects.all()
        return render(request,'blog/profile.html',{'datas':datas,'name':request.user.get_full_name})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Post added successfully.')
                form = PostForm()
        else:
            form = PostForm()
        return render(request,'blog/addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def updatepost(request,id):
    if request.user.is_authenticated:
        post = Post.objects.get(pk=id)
        if request.method == 'POST':
            form = PostForm(request.POST,instance=post)
            if form.is_valid():
                form.save()
                messages.success(request,'Update Successfully.')
                form = PostForm()
        else:
            form = PostForm(instance=post)
        return render(request,'blog/updatepost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            post.delete()
            messages.success(request,'Post Deleted Successfully.')
            return HttpResponseRedirect('/profile/')
    else:
        return HttpResponseRedirect('/home/')
# interchange dash board with profile
def dashboard(request,id):
    user = User.objects.get(pk=id)
    return render(request,'blog/dashboard.html',{'user':user})

def dashboardchange(request,id):
    if request.user.is_authenticated:
        user = User.objects.get(pk=id)
        if request.method == 'POST':
            form = DashBoardChange(request.POST,instance=user)
            if form.is_valid():
                form.save()
                messages.success(request,'Updated Successfully.')
        else:
            form = DashBoardChange(instance=user)
        return render(request,'blog/changedashboard.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Password Changed Successfully.')
            return HttpResponseRedirect('/profile/')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'blog/passwordchange.html',{'form':form})

    


