from django.shortcuts import render
from django.views.generic import ListView


def index(requests):
    return render(requests, 'articles/index.html')


