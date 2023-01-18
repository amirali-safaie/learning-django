from django.contrib.auth import views
from django.urls import path
from .views import Home,Create,Update,Delete,Preview

app_name="account"


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout")
]

urlpatterns+=[
    # path("",home,name="home"),
    path("",Home.as_view(),name="home"),
    path("create_article/",Create.as_view(),name="create"),
    path("update_article/<int:pk>",Update.as_view(),name="update"), #pk پرایمری کی توی دیتابیس برای هر مقاله
    path("delete_article/<int:pk>",Delete.as_view(),name="delete"), #pk پرایمری کی توی دیتابیس برای هر مقاله
    path("preview_article/<int:pk>",Preview.as_view(),name="preview"), #pk پرایمری کی توی دیتابیس برای هر مقاله
]
