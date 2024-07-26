from lib2to3.fixes.fix_input import context

from django.shortcuts import render

from .models import Movies_Info


# from django.http import HttpResponse
# Create your views here.
def home_page(requset):
    return render(requset ,"base.html",)
def welcome_page(request):
    return render(request, "MoviesListApp/about.html" )

def Movies_list(request):
    Movies = Movies_Info.objects.all()
    Movies_list = []
    for Movie in Movies:
        Movies_list.append({'movie':Movie})
    context = {"Movies_list": Movies_list}
    return render(request,"MoviesListApp/Movies_list.html", context)