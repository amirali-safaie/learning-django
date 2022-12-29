from django.http import Http404


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
    """چه پستی هایی را در پنل ادمین خودم به چه کاربری نمایش بدم"""
    def form_valid(self,form):
        if self.request.user.is_superuser :
            form.save()
        else: 
            self.obj = form.save(commit = False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)  