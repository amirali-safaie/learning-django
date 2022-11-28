from django.shortcuts import HttpResponse, render,get_object_or_404
from django.http import HttpRequest
from .models import Article,Category
from django.core.paginator import Paginator
from django.views.generic import ListView






def home(request,page=1):
    """this is a test for views"""
    post_list = Article.objects.filter(status="p").order_by('publish')
    pageinator = Paginator(post_list,5)
    post = pageinator.get_page(page)
    print(post.next_page_number)
    posts= {
        "posts": post
    }

    return render(request,"htmls_file/home.html",posts)





def details(request,slug):
    """this is special page for each post """
    posts_details= {
        "post_detail":get_object_or_404(Article,slug=slug,status="p")
    }

    return render(request,"htmls_file/details.html",posts_details)





def category(request,slug):
    """this is special page for each post realted to scecial category """
    category_list= {
        "category":get_object_or_404(Category,slug=slug,status=True)
    }
    return render(request,"htmls_file/category.html",category_list)
# Create your views here.
