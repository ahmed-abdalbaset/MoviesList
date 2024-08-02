from audioop import reverse
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
        reviews =Movie.review_set_all()
        if reviews:
            Movi_rating = average_rating([review.rating for review in reviews])
            number_of_reviews= len(reviews)
        else:
            Movie_rating = None
            number_of_reviews = 0
        Movies_list.append({'movie':Movie})
    context = {"Movies_list": Movies_list}
    return render(request,"MoviesListApp/Movies_list.html", context)