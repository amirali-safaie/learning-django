from django.db import models
from django.utils import timezone




class Article(models.Model):
    STATUS_CHOICES=(
        ('d','draft'),
        ("p",'publish')
    )


    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True)
    descriptions = models.TextField()
    publish= models.DateField(default=timezone.now)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES)


    def __str__(self):
        return self.title

# Create your models here.
