


from django.shortcuts import render
from blogs.models import Blog, Category


def home(request):
    categories=Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True).order_by('-updated_at')
    posts=Blog.objects.filter(is_featured=False, status=1)
    
   
    context={
        'categories': categories,
        'featured_post':featured_post,
        'posts':posts
       
    }
    return render (request, 'home.html', context)