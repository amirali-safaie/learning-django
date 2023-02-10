from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  
from django.shortcuts import render, redirect  
from django.http import HttpResponse  
from django.utils.encoding import force_bytes,force_str 
from .forms import SignupForm  
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode  
from django.template.loader import render_to_string  
from .tokens import account_activation_token  
from django.core.mail import EmailMessage  
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,PasswordChangeView
from .mixins import (
    FieldMixin,
    FormValidMixin,
    AuthorAccessUpdate,
    Superuseraccess,
    Access
)
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

class Login(LoginView):
    """ویو لاگین ساختم از لاگین جنگو ارث بری کردم"""
    def get_success_url(self):  # این متد میگه بعد از لاگین کردن کجا بریم 
        user = self.request.user
        if user.is_superuser or user.is_author:
            return reverse_lazy("account:home")
        else:
            return reverse_lazy("account:make_profile")

class ChangePassword(PasswordChangeView):
    """ویو برای اینکه پسورد رو عوض کینم و از چینگ پسورد جنگو ارث بری میکنه"""

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your password has been changed.")
        return super(PasswordChangeView, self).form_valid(form)


    success_url = reverse_lazy("account:make_profile")
    template_name = "registration/change_pass.html"








class Register(CreateView):
    form_class = SignupForm
    template_name = "registration/register.html"
    def form_valid(self, form):
            # save form in the memory not in database  
            user = form.save(commit=False)  
            user.is_active = False  
            user.save()  
            # to get the domain of the current site  
            current_site = get_current_site(self.request)  
            mail_subject = 'Activation link has been sent to your email id'  
            message = render_to_string('registration/activate_account.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMessage(  
                        mail_subject, message, to=[to_email]  
            )  
            email.send()  
            return HttpResponse('Please confirm your email address to complete the registration')  






#..........register with FBV ............

  
# def signup(request):  
#     if request.method == 'POST':  
#         form = SignupForm(request.POST)  
#         if form.is_valid():  
#             # save form in the memory not in database  
#             user = form.save(commit=False)  
#             user.is_active = False  
#             user.save()  
#             # to get the domain of the current site  
#             current_site = get_current_site(request)  
#             mail_subject = 'Activation link has been sent to your email id'  
#             message = render_to_string('acc_active_email.html', {  
#                 'user': user,  
#                 'domain': current_site.domain,  
#                 'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
#                 'token':account_activation_token.make_token(user),  
#             })  
#             to_email = form.cleaned_data.get('email')  
#             email = EmailMessage(  
#                         mail_subject, message, to=[to_email]  
#             )  
#             email.send()  
#             return HttpResponse('Please confirm your email address to complete the registration')  
#     else:  
#         form = SignupForm()  
#     return render(request, 'signup.html', {'form': form})  






def activate(request, uidb64, token):# this view check url is valid or not and user is corroct or not
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        context = {'uidb64': uidb64, 'token': token} 
        
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        # return HttpResponse('Thank you for your email confirmation. Now you can login your account <a href="{%url "loging"%}">log in</a>.')

        return render(request, 'registration/thank_confirm.html', context)
    else:
        return HttpResponse('Activation link is invalid! <a href = "{% url "register"%}">sign up</a>')