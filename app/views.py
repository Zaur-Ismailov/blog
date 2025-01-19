from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts': posts})

def post(request, pk):
    post_data = Post.objects.get(id=pk)
    return render(request,'post.html', {'post': post_data})
@login_required(login_url='users:log_in')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect ('app:home')
    
    return render (request, 'post_form.html', {'form': form})

@login_required(login_url='users:log_in')
def edit_post(request, pk):
    
    post_data= Post.objects.get(id=pk)
    
    if request.user != post_data.author:
        return render (request, '403.html')
    form = PostForm(request.POST or None, request.FILES or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('app:post', pk=pk)
    

    return render(request, 'post_form.html', {'form': form})

@login_required(login_url='users:log_in')
def delete_post(request, pk):
    post_data=Post.objects.get(id=pk)

    if request.user != post_data.author:
        return render (request, '403.html')  

    if request.method == 'POST':
        post_data.delete()
        return redirect ('app:home')
    
    return render(request, 'delete_post.html', {'pk': pk})

def post_like(request, pk):
    post_data=Post.objects.get(pk=pk)
    user = request.user
    
    if user not in post_data.likes.all():
        post_data.likes.add(user)
        post_data.dislikes.remove(user)
    elif user in post_data.likes.all():
        post_data.likes.remove(user)
    return redirect('app:post', pk=post_data.pk) 
    
def post_dislike(requst, pk):
    post_data=Post.objects.get(pk=pk)
    user = requst.user
    
    if user not in post_data.dislikes.all():
        post_data.dislikes.add(user)
        post_data.likes.remove(user)
    elif user in post_data.dislikes.all():
        post_data.dislikes.remove(user)
    return redirect('app:post', pk=post_data.pk)

