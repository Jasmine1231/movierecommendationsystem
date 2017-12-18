from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^(?P<movie>[\d]+/$',views.movie_info,name='movie_info'),
]