from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def allblogs(request):
    blogs = Blog.objects
    # stored allblogs.html in blog folder under templates to prevent different apps
    # having same file name
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

# Accepts user-inputted blog_id (from url path) and retrieves corresponding object
# if available. If not a 404 error is returned.
def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
