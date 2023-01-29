from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .mixins import FieldMixin,FormValidMixin,AuthorAccessUpdate,Superuseraccess,Access
from .forms import ProfileForm
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView
)
from blog.models import Article
from .models import User
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



# @login_required   #این دکریتور میگه اگر میخوای از این ویو استفاده کنی باید لاگ این کنیfrom django.shortcuts import render,redirect
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

class Home(Access,ListView):

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()  #گرفتن پست ها از مدل
        else:
            return Article.objects.filter(author = self.request.user)
    template_name="registration/home.html" #این ویو چه تمپلیتی را نمایش دهد


# @login_required   #این دکریتور میگه اگر میخوای از این ویو استفاده کنی باید لاگ این کنی
# def home(request):
#     return render(request,"registration/home.html")


class Create(Access,FieldMixin,FormValidMixin,CreateView):#این ویو برای وارد کردن اطلاعات توی مدلِ ( نوشتن مقاله )
    model = Article
    template_name = "registration/create_article.html"


class Update(AuthorAccessUpdate,FieldMixin,FormValidMixin,UpdateView):
    """این ویو برای اپدیت و ادیت مقالات نوشته شده"""
    model = Article
    template_name = "registration/create_article.html"

class Delete(Superuseraccess,DeleteView):
    """این ویو برای پاک کردن مقاله و پست """
    model = Article
    success_url = reverse_lazy("account:home")
    template_name = "registration/delete_article.html"


class Preview(AuthorAccessUpdate,DetailView):
    """این ویو برای دیدن پریویو پست هایی که میخوایم نمیایش بدیم"""
    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return get_object_or_404(Article,pk=pk)#خودش میره دنبلا تمپلیتی که از ترکیب دیتیل و ارتیکل باشه
    model = Article
        

class MakeProfile(LoginRequiredMixin,UpdateView):
    """این ویو برای درست کردن پروفایل کاربری نوشته شده"""
    model = User  #از مدل یوزر که در اکانت درست کردیم استفاده میکنه که اونم از یوزر خود جنگو ارث بری میکنه
    form_class = ProfileForm
    template_name = "registration/make_profile.html"

    success_url = reverse_lazy("account:home")

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk) #پروفایل کسی رو بگیره که pk با pk یوزری که توی سایته برابر

    def get_form_kwargs(self):#تابع برای فرستادن یوزر به فرم  
        kwrgs =  super(MakeProfile,self).get_form_kwargs() 
        kwrgs.update({
            "user":self.request.user
        })
        return kwrgs #فرستادن یوزر به عنوان عضوی از کی ورد ارگیومنت ها

class Login(LoginView): #ویو لاگین ساختم از لاگین جنگو ارث بری کردم
    def get_success_url(self):  # این متد میگه بعد از لاگین کردن کجا بریم 
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:make_profile")