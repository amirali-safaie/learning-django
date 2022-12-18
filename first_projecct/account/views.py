from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView
from blog.models import Article
# from django.http import HttpResponse
# from django.contrib.auth import authenticate,login,logout
# from django.contrib import messages
# # Create your views here.
# def login_user(request):
#     # print(request.POST)
#     # username = request.POST.get('username')
#     # print(username)
#     # password = request.POST.get('password')
#     # print(password)

#     if request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request,username=username,password=password)
#         if user is not None :
#             print(user)
#             login(request,user)
#             return redirect("/")
#         else:
#             messages.info(request,'wronge username or pass ')
#             return redirect('account:login_user')

#     return render(request,'account/index.html')


# def logout_user(request):
#     logout(request)
#     return redirect('account:login_user')

class Home(LoginRequiredMixin,ListView):

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()  #گرفتن پست ها از مدل 
        else:
            return Article.objects.filter(author = self.request.user)
    template_name="registration/home.html" #این ویو چه تمپلیتی را نمایش دهد


# @login_required   #این دکریتور میگه اگر میخوای از این ویو استفاده کنی باید لاگ این کنی
# def home(request):
#     return render(request,"registration/home.html")


class Create(LoginRequiredMixin,CreateView):
    model = Article
    fields = ["author","title","slug","category","publish","status","descriptions"]
    template_name = "registration/create_article.html"

