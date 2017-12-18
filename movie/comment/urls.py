from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.movie_list,name='movie_list'),
    url(r'^(?P<m_id>[0-9]+)/$',views.movie_info,name='movie_info'),
]