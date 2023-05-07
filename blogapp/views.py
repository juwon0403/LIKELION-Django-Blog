from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def new(request):
    return render(request, 'new.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def mbtitest(request):
    return render(request, 'mbtitest.html')

def mbtiresult(request):
    return render(request, 'mbtiresult.html')

def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('login')

def formcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('login')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form' : form})


def modelformcreate(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form' : form})