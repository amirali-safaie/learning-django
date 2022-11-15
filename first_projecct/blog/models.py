from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User




class Article(models.Model):
    STATUS_CHOICES=(
        ('d','draft'),
        ("p",'publish')
    )

    creator = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    descriptions = models.TextField()
    publish= models.DateField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)


    def __str__(self):
        return self.title


# class LogDelet(object):
#




# Create your models here.
