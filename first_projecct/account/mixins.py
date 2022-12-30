from django.http import Http404
from django.shortcuts import HttpResponse, render,get_object_or_404
from blog.models import Article


class FieldMixin():
    """چه پستی هایی را در پنل ادمین خودم به چه کاربری نمایش بدم"""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser : 
            self.fields = ["author","title","slug","category","publish","status","descriptions"]
        elif request.user.is_author:
            self.fields = ["title","slug","category","publish","descriptions"]
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
    """کاربر فقط به پست خودش برای ادیت کردن دسترسی داشته باشه بجز سوپر یوزر که به همه داره"""
    def dispatch(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if((article.author == request.user and article.status == 'd') or request.user.is_superuser):
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("invalid url")
