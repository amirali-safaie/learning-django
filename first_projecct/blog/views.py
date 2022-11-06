from django.shortcuts import HttpResponse, render
from django.http import HttpRequest
from .models import Article







def home(request):
    """this is a test for views"""
    posts= {
        "post": Article.objects.filter(status="p").order_by('publish')
    }

    return render(request,"htmls_file/home.html",posts)


def details(request,slug):
    """this is index page for web site """
    posts_details= {
        "post_detail": Article.objects.get(slug=slug)
    }

    return render(request,"htmls_file/details.html",posts_details)
# Create your views here.
