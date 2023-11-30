
from django.http import HttpResponse
from django.shortcuts import render
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


# output = ', '.join([m.title for m in movies]) affichage 
# par url  des title de movies  
# return HttpResponse(output)

