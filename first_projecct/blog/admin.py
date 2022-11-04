from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug",'publish')
    list_filter = ('publish','status')
    search_fields = ('title','descriptions')


admin.site.register(Article,ArticleAdmin)
# Register your models here.
