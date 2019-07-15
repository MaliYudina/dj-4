from django.urls import path

from .views import *

urlpatterns = [
    path('articles/read/<str:name>', one_article, name='one_article'),
    path('articles/', all_articles, name='all_articles'),
]

