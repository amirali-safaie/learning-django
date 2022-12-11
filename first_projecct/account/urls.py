from django.contrib.auth import views
from django.urls import path
from .views import Home

app_name="account"


urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
]

urlpatterns+=[
    # path("",home,name="home"),
    path("",Home.as_view(),name="home")
]
