from django.urls import path
from .views import home,details,category

app_name = "blog"
urlpatterns = [
    path('',home,name="home"),
    path('post/<slug:slug>',details,name="details"),
    path('category/<slug:slug>',category,name="category")
]
