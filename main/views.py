from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout
from .forms import PostForm,RegisterForm
from .models import Post

# Create your views here.


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url="/login")
def home(request):
    user_id = request.user.id
    posts = Post.objects.filter(author_id = user_id)
    return render (request,'main/home.html',{"posts":posts})



@login_required(login_url="/login")
def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()

    return render(request, 'main/post.html', {"form": form})

@login_required(login_url="/login")
def edit_post(request,post_id):
    posts = Post.objects.get(id=post_id)
    if request.method != 'POST':
        form = PostForm(instance=posts)

    else:
        
        form = PostForm(request.POST,instance=posts) 
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'main/post.html', {"form": form})

@login_required(login_url="/login")
def delete_post(request,post_id=None):
    post_to_delete=Post.objects.get(id=post_id)
    post_to_delete.delete()
    return redirect('home')

