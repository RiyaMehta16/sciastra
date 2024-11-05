# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from django.contrib import messages
from .forms import UserRegisterForm

def blog_list(request):
    posts = BlogPost.objects.filter(is_published=True).order_by('-published_date')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'blog/blog_detail.html', {'post': post})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog_list')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {'form': form})
