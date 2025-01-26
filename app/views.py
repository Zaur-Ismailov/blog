from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html',{'posts': posts})

def post(request, pk):
    post_data = Post.objects.get(id=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        if request.user.is_anonymous:
            return redirect('users:log_in')
        
        comment = form.save(commit=False)
        comment.post = post_data
        comment.author = request.user
        comment.save()
        return redirect('app:post', pk=post_data.pk)


    return render(request,'post.html', {'post': post_data, 'form':form})




@login_required(login_url='users:log_in')
def create_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect ('app:home')
    
    return render (request, 'form.html', {'form': form})

@login_required(login_url='users:log_in')
def edit_post(request, pk):
    
    post_data= Post.objects.get(id=pk)
    
    if request.user != post_data.author:
        return render (request, '403.html')
    form = PostForm(request.POST or None, request.FILES or None, instance=post_data)
    if form.is_valid():
        form.save()
        return redirect('app:post', pk=pk)
    

    return render(request, 'form.html', {'form': form})

@login_required(login_url='users:log_in')
def delete_post(request, pk):
    post_data=Post.objects.get(id=pk)

    if request.user != post_data.author:
        return render (request, '403.html')  

    if request.method == 'POST':
        post_data.delete()
        return redirect ('app:home')
    
    return render(request, 'delete_post.html', {'pk': pk})

@login_required(login_url='users:log_in')
def post_like(request, pk):
    post_data=Post.objects.get(pk=pk)
    user = request.user
    
    if user not in post_data.likes.all():
        post_data.likes.add(user)
        post_data.dislikes.remove(user)
    elif user in post_data.likes.all():
        post_data.likes.remove(user)
    return redirect('app:post', pk=post_data.pk) 

@login_required(login_url='users:log_in')    
def post_dislike(requst, pk):
    post_data=Post.objects.get(pk=pk)
    user = requst.user
    
    if user not in post_data.dislikes.all():
        post_data.dislikes.add(user)
        post_data.likes.remove(user)
    elif user in post_data.dislikes.all():
        post_data.dislikes.remove(user)
    return redirect('app:post', pk=post_data.pk)


def comment_like(request,pk):
    comment = Comment.objects.get(pk=pk)
    user = request.user
    likes = comment.likes

    if user not in likes.all():
        likes.add(user)
        comment.dislikes.remove(user)
    elif user in likes.all():
        likes.remove(user)
    return redirect('app:post', pk=comment.post.pk)

def comment_dislike(request, pk):
    comment = Comment.objects.get(pk=pk)
    user = request.user
    dislikes = comment.dislikes

    if user not in dislikes.all():
        dislikes.add(user)
        comment.likes.remove(user)
    elif user in dislikes.all():
        dislikes.remove(user)
    return redirect('app:post', pk=comment.post.pk)


def comment_edit(request,pk):
    comment = Comment.objects.get(pk=pk)
    form = CommentForm(request.POST or  None, instance=comment)

    if form.is_valid():
        comment=form.save(commit=False)
        if not comment.updated:
            comment.updated = True
        comment.save()
        return redirect('app:post', pk=comment.post.pk)
    
    return render(request, 'form.html', {'form':form})

def comment_delete(request,pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        comment.delete()
        return redirect('app:post', pk=comment.post.pk)
    return render(request, 'comment_delete.html', {'comment':comment})

@login_required(login_url='users:log_in')  
def reply(request, pk):
    
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        
        parent_comment = Comment.objects.get(pk=pk)
        instance = form.save(commit=False)

        instance.post = parent_comment.post
        instance.author = request.user
        instance.parent = parent_comment
        instance.save()
        return redirect('app:post', pk=parent_comment.post.pk)
    
    return render(request, 'form.html', {'form':form})

@login_required(login_url='users:log_in') 
def read_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    return render(request, 'read_comment.html', {'comment':comment})