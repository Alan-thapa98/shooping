# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def shop(request):
    hello = "these is the shop"
    context = {
        'hello': hello,
    }
    return render(request, 'shop.html', context)


def cats(request):
    hello = "these is the cats"
    context = {
        'hello': hello,
    }
    return render(request, 'cats.html', context)


def cats_views(request):
    hello = "these is the cats_views"
    context = {
        'hello': hello,
    }
    return render(request, 'cats_views.html', context)


def cart(request):
    hello = "these is the cart"
    context = {
        'hello': hello,
    }
    return render(request, 'cart.html', context)


def payment_and_summery(request):
    hello = "these is the payment_and_summery"
    context = {
        'hello': hello,
    }
    return render(request, 'payment_and_summery.html', context)
