from django.shortcuts import HttpResponse, render,get_object_or_404
from django.http import HttpRequest
from .models import Article,Category







def home(request):
    """this is a test for views"""
    posts= {
        "posts": Article.objects.filter(status="p").order_by('publish')
    }

    return render(request,"htmls_file/home.html",posts)


def details(request,slug):
    """this is special page for each post """
    posts_details= {
        "post_detail":get_object_or_404(Article,slug=slug,status="p")
        # "post_detail": Article.objects.get(slug=slug)
    }

    return render(request,"htmls_file/details.html",posts_details)
# Create your views here.
