from django.urls import path
from .views import *

urlpatterns = [
    path('', shop, name='shop'),
    path('cats', cats, name='cats'),
    path('cats_views', cats_views, name='cats_views'),
    path('cart', cart, name='cart'),
    path('payment_and_summery', payment_and_summery, name='payment_and_summery'),


]
