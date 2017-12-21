from django.shortcuts import render,get_object_or_404
from .models import MovieInfo,Sentimentclassify,ShortComments
from django.http import HttpResponse
from django.template import loader
from django.core.paginator import Paginator

# Create your views here.
def movie_list(request):
    movies = MovieInfo.objects.all()
    limit=200
    paginatior=Paginator(movies,limit)
    page=request.GET.get('page',1)
    loaded=paginatior.page(page)
    return render(request, "../templates/movie/list.html", {'movies': loaded})


def movie_info(request,m_id):
    movie=get_object_or_404(MovieInfo, m_id=m_id)
    return render(request,'../templates/movie/single_movie/info.html',{'movie':movie})


def sentiment_classify(request,m_id):
    movie = get_object_or_404(MovieInfo,m_id=m_id)
    sentiment=get_object_or_404(Sentimentclassify,m=m_id)
    comments = ShortComments.objects.filter(m=m_id).first()
    return render(request,'../templates/html/single_film.html',{'sentiment':sentiment,'movie':movie,'comments':comments})


def show_index(request):
    movien=MovieInfo.objects
    return render(request,'../templates/index.html', {'m': movien})