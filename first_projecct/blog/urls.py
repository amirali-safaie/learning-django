from django.urls import path
from .views import home,Details,Category_list

app_name = "blog"
urlpatterns = [
    path('',home.as_view(),name="home"),
    path('page/<int:page>',home.as_view(),name="home"),
    path('post/<slug:slug>',Details.as_view(),name="Details"),
    path('category/<slug:slug>',Category_list.as_view(),name="category"),
    path('category/<slug:slug>/page/<int:page>',Category_list.as_view(),name="category")
]
