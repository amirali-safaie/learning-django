from django.shortcuts import HttpResponse, render
from django.http import HttpRequest


people = {
    "people":[
    {
        "name":"amirali",
        "family":"safaie"
    },
    {
        "name":"mohammad",
        "family":"safaie"
    }
    ]

}




def home(request):
    """this is a test for views"""

    return render(request,"home.html",people)

# Create your views here.
