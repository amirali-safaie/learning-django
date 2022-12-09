from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extensions.utils import jalali_converter


#make manager ...................

class PostManager(models.Manager): #درست کردن منیجیر برای نمایش مقاله های پابلیش
    def published(self):
        return self.filter(status="p")

class categorytManager(models.Manager):#درست کردن منیجیر برای نمایش دسته بندی  های فعال
    def active(self):
        return self.filter(status=True)


#make manager ...................




#category class ...............
class Category(models.Model):
    """مدل کتگوری ها """
    parent = models.ForeignKey("self",default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name='children')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=True,verbose_name="show")
    position = models.IntegerField(verbose_name="order")

    class Meta:
        ordering = ['parent__id','position']

    def __str__(self):
        return self.title

    objects = categorytManager()

#category class ...............





#article class ................
class Article(models.Model):
    STATUS_CHOICES=(
        ('d','draft'),
        ("p",'publish')
    )

    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="posts_of_author")# اختصاص دادن یک نویسدنده برای پست
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    category = models.ManyToManyField(Category,related_name="post_of_category")
    descriptions = models.TextField()
    publish= models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)


    class Meta:
        ordering = ["-publish"]

    def jalali_get_publish(self):
         return jalali_converter(self.publish)

    jalali_get_publish.short_description = "date published"

    def show_category(self):
        return self.category.active()

    def __str__(self):
        return self.title

    objects = PostManager()
#article class ................

    



# class LogDelet(object):
#




# Create your models here.
