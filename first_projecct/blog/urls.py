from django.urls import path
from .views import home,details

app_name = "blog"
urlpatterns = [
    path('',home,name="home"),
    path('post/<slug:slug>',details,name="details")
]
