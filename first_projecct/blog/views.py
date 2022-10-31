from django.shortcuts import HttpResponse, render
from django.http import HttpRequest

def home(request):
    """this is a test for views"""
    context = {
        "names" : [
            {"name":"amirali"},
            {"name":"mohammad"}
        ]
        ,
        "familys" : [
            {"family":"safaie"},
            {"family":"movahed"}
        ]
            }
    return render(request,'home.html', context)
# Create your views here.
