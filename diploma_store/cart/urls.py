
from django.urls import path

from .views import *


urlpatterns = [
    path('add/', create_or_update_cart_view, name='create_cart'),
    path('', cart_view, name='cart'),
]
