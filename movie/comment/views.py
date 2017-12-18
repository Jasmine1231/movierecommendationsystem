from django.shortcuts import render,get_object_or_404
from .models import MovieInfo
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def movie_list(request):
    movies = MovieInfo.objects.all()
    context={

    }
    return render(request, "../templates/movie/list.html", movies)


def movie_info(request,m_id):
    movie=get_object_or_404(MovieInfo,pk=m_id)
    return render(request,'movie/single_movie/info.html',{'movie':movie})