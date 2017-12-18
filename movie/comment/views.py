from django.shortcuts import render,get_object_or_404
from .models import Sentimentclassify

# Create your views here.
def movie_info(request,m):
    movie=get_object_or_404(Sentimentclassify,m=m)
    return render(request,'movie/single_film.html',{'movie':movie})