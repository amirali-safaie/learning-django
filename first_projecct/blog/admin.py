from django.contrib import admin
from .models import Article,Category

@admin.action(description="make post publihs")
def make_publish(modeladmin,request,queryset):
    queryset.update(status='p')
    rows_update = queryset.update(status='p')
    if rows_update == 1:
        message_bit = "1 post published"
    else:
        message_bit = "%s posts publihsed" %rows_update
    
    modeladmin.message_user(request,"%s " %message_bit)





@admin.action(description="make post draft")
def make_draf(modeladmin,request,queryset):
    """اکشن پیش نویس کردن پست"""
    queryset.update(status='d')
    rows_update = queryset.update(status='d')
    if rows_update == 1:
        message_bit = "1 post drafted"
    else:
        message_bit = "%s post drafted" %rows_update
    
    modeladmin.message_user(request,"%s " %message_bit)




@admin.action(description="make category deactive")
def make_deactive(modeladmin,request,queryset):
    """اکشن غیرفال کردن کتگوری"""
    queryset.update(status=False)


@admin.action(description="make category active")
def make_active(modeladmin,request,queryset):
    queryset.update(status=True)





class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title","slug",'jalali_get_publish',"author","is_special",'status','category_to_str')
    list_filter = ('publish','status')
    search_fields = ('title','descriptions')
    prepopulated_fields = { 'slug': ('title',)}
    actions = [make_publish,make_draf]



admin.site.register(Article,ArticleAdmin)





class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title","slug",'status','parent')
    list_filter = ('status',)
    search_fields = ('title',)
    prepopulated_fields = { 'slug': ('title',)}
    actions = [make_deactive,make_active]


admin.site.register(Category,CategoryAdmin)
# Register your models here.




