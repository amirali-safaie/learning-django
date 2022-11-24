from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extensions.utils import jalali_converter


#category class ...............
class Category(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    status = models.BooleanField(default=True,verbose_name="show")
    position = models.IntegerField(verbose_name="order")

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.title

#category class ...............





#article class ................
class Article(models.Model):
    STATUS_CHOICES=(
        ('d','draft'),
        ("p",'publish')
    )

    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    category = models.ManyToManyField(Category)
    descriptions = models.TextField()
    publish= models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)


    class Meta:
        ordering = ["-publish"]


    # class Meta:
    #     verbose_name = "مقاله"
    #     verbose_name_plural = "مقالات"

    def jalali_get_publish(self):
         return jalali_converter(self.publish)

    jalali_get_publish.short_description = "date published"

    def __str__(self):
        return self.title
#article class ................

    



# class LogDelet(object):
#




# Create your models here.
