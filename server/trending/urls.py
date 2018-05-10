from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'insta', views.insta, name='insta'),
    url(r'fb', views.fb, name='fb'),
    url(r'youtube', views.youtube, name='youtube'),
    url(r'tweeter', views.tweet, name='tweet'),
    url(r'news', views.news, name='news'),
]
