from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Cinema(request):
    return HttpResponse('<button><marquee><h1>INTROVERT MOVIE LOVERS ARE ALWAYS GREAT AT ONE SIDE LOVE</h1></marquee></button>')