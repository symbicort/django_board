from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


def index(request):
    post_lists = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'posts': post_lists})


@login_required(login_url='/user/login')
@csrf_exempt
def post_write(request):
    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, 'post_write.html', context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)
        print(request.user)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.author = request.user
            post.save()
        else:
            print("에러 발생", postForm.errors, request.user)
        return redirect('/detail/' + str(post.id))


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    commentForm = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'commentForm' : commentForm })


def post_delete(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect('/')
    post.delete()
    return redirect('/')


@csrf_exempt
def post_update(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        postForm = PostForm(instance=post)
        context = {'postForm': postForm}

        return render(request, 'post_write.html', context)

    elif request.method == "POST":
        postForm = PostForm(request.POST, instance=post)
        if postForm.is_valid():
            post = postForm.save(commit=False)
            post.save()

        return redirect('/detail' + int(post.id))

@login_required(login_url='/user/login')
@csrf_exempt
def comment_write(request, post_id):
    commentForm = CommentForm(request.POST)
    if(commentForm.is_valid()):
        comment = commentForm.save(commit=False)
        post = Post.objects.get(id=post_id)
        comment.post = post
        comment.author = request.user
        comment.save()
        return redirect('/detail/' + str(post.id))
    else:
        print("에러 발생", commentForm.errors)
