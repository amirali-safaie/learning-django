from django.shortcuts import HttpResponse, render,get_object_or_404
from django.http import HttpRequest
from .models import Article,Category
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from django.views.generic import ListView





class home(ListView):
    queryset = Article.objects.published()
    paginate_by = 5

#home functionbase...........///////////////////////////////////////////////
# def home(request,page=1):
#     """this is a test for views"""
#     post_list = Article.objects.filter(status="p").order_by('publish')
#     pageinator = Paginator(post_list,5)
#     post = pageinator.get_page(page)
#     print(post.next_page_number)
#     posts= {
#         "posts": post
#     }

#     return render(request,"htmls_file/home.html",posts)
#home functionbase...........///////////////////////////////////////////////



class Details(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Article.objects.published(),slug=slug)


#detail functionbase...........///////////////////////////////////////////////
# def details(request,slug):
#     """this is special page for each post """
#     posts_details= {
#         "post_detail":get_object_or_404(Article,slug=slug,status="p")
#     }

#     return render(request,"blog/details.html",posts_details)
#detail functionbase...........///////////////////////////////////////////////





class Category_list(ListView):
    paginate_by = 5  # """پیچ انیشین صفجه کتگوری"""
    template_name = "blog/category.html"

    def get_queryset(self):
        global category
        slug = self.kwargs.get("slug")
        category = get_object_or_404(Category.objects.active(),slug=slug)
        return category.post_of_category.published()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = category
        return context





class author_list(ListView):
    paginate_by = 3  # """پیچ انیشین صفجه کتگوری"""
    template_name = "blog/author_list.html"   #نشان دادن این ویو بر روی این تمپلیت

    def get_queryset(self):
        global author
        username = self.kwargs.get("username") 
        author = get_object_or_404(User,username=username) #گرفتن یوزر هایی که یوزرنیمشون رو وارد میکنیم
        return author.posts_of_author.published()#گرفتن پست های اون نویسنده(یوزر)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = author
        return context
    


#category functionbase...........///////////////////////////////////////////////
# def category(request,slug,page=1):
#     """this is special page for each post realted to scecial category """
#     category = get_object_or_404(Category,slug=slug)
#     post_list = category.post_of_category.published()
#     pageinator = Paginator(post_list,5)
#     posts = pageinator.get_page(page)
#     category_list= {
#         "category":category,
#         "posts":posts
#     }
#     return render(request,"blog/category.html",category_list)
#category functionbase...........///////////////////////////////////////////////



        
    