from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
template_files = {
    "index": "index.html",
    "top-sellers": "top-sellers.html",
    "advertisement-post": "advertisement-post.html",
    "register": "register.html",
    "login": "login.html",
    "profile": "profile.html"
}

def basic_view(name) -> (...):
    def function (request):
        return render(request, template_files[name])

    return function
