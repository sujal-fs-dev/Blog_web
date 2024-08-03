from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Blog
from .models import Category


# Create your views here.

def post_by_category(request, category_id):
    #fatch the post that belongs to the category with the id
    posts=Blog.objects.filter(status=1, category=category_id)
   # category=Category.objects.get(pk=category_id)
    category=get_object_or_404(Category, id=category_id)

    context={
        'posts':posts,
        'category':category,
    }
    return render(request,'posts_by_category.html', context)

def blogs(request, slug):
    single_blog=get_object_or_404(Blog, slug=slug, status=1)
    context={
        'single_blog':single_blog

    }
    return render (request,'blogs.html',context)
