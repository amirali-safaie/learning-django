"""first_projecct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include,re_path
from account.views import Login,ChangePassword,Register,activate



urlpatterns = [
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path("",include('blog.urls'),name='blog'),
    path("account/",include('account.urls'),name='account'),
    path("",include('django.contrib.auth.urls')),
    path("login/", Login.as_view(), name="login"),
    path("change_password/",ChangePassword.as_view(),name="change_password"), #یو ار ال تغییر پسورد


    path("register/", Register.as_view(), name="register"),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',activate, name='activate'),
    path('activate/<slug:uidb64>/<slug:token>/',activate, name='activate')
]
