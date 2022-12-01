from django.contrib import admin
from .models import Article,Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug",'jalali_get_publish','status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','descriptions')
    prepopulated_fields = { 'slug': ('title',)}


    def category_to_str(self,obj):
        return ", ".join(category.title for category in obj.category.all())
    category_to_str.short_description = "category"


admin.site.register(Article,ArticleAdmin)





class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","slug",'status','parent')
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = { 'slug': ('title',)}


admin.site.register(Category,CategoryAdmin)
# Register your models here.




