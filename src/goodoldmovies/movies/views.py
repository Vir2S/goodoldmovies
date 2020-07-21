from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View


movies = {
    'catchfire': {
        'title': 'Catchfire',
        'year': 1990,
    },
    'mighty-ducks': {
        'title': 'Mighty Ducks the Movie: The First Face-Off',
        'year': 1997,
    },
    'le-zombi': {
        'title': 'Le Zombi de Cap-Rouge',
        'year': 1997,
    },
}


class MovieView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request, 'movies/index.html', context={
                'director': settings.DIRECTOR,
                'movies': movies,
            }
        )


class MainPageView(View):
    def get(self, request, *args, **kwargs):
        html = '\n'.join(f'<div>{movie}</div>' for movie in movies)
        return HttpResponse(html)


class MovieDetailView(View):
    def get(self, request, movie_name, *args, **kwargs):
        if movie_name not in movies:
            raise Http404

        movie_info = "".join(
            f'<tr><td>{key}:</td><td>{value}</td></tr>'
            for key, value in movies[movie_name].items()
        )
        return HttpResponse(f'<table><tbody>{movie_info}</tbody></table>')