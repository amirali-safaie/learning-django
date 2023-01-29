from django.http import Http404
from django.shortcuts import HttpResponse, render,get_object_or_404,redirect
from blog.models import Article


class FieldMixin():
    """چه فیلد هایی رو به چه نوع کاربر هایی نشون بده"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser :
            self.fields = ["author","title","slug","category","publish","is_special","status","descriptions"]
        elif request.user.is_author:
            self.fields = ["title","slug","category","publish","is_special","descriptions"]
        else:
            raise Http404
        return super().dispatch(request, *args, **kwargs)

class FormValidMixin():
    """برای کاربرانی که دسترسی به نویسنده و وضعیت مقاله ندارن نویسنده و وضعیت چجوری سیو بشه"""
    def form_valid(self,form):
        if self.request.user.is_superuser :
            form.save()
        else:
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)


class AuthorAccessUpdate():
    """کاربر فقط به پست خودش  دسترسی داشته باشه بجز سوپر یوزر که به همه داره"""
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if((article.author == request.user and article.status in ['d','b']) or request.user.is_superuser):#اگر مقاله پیش نویس یا برگشته داده شده بود میشه
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("invalid url")

class Access():
    """کاربر به کجاها دسترسی داره و اگر به فلان یو ار ال دسترسی نداره کجا بره"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user.is_author:#
            return super().dispatch(request, *args, **kwargs)
        else:
            return redirect("account:make_profile")



class Superuseraccess():
    """فقط سوپر یوزر بتونه یک پست رو پاک کنه"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("invalid url")
