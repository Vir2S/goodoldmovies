"""goodoldmovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movies.views import MovieView, MainPageView, MovieDetailView, ProducerView, FilmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieView.as_view()),
    # path('producers/', ProducerView.as_view()),
    path('producers/<int:year>/', ProducerView.as_view()),
    path('producers/<int:year>/<int:month>', ProducerView.as_view()),
    # path('movies/', include('movies.urls')),
    path("movies/", MainPageView.as_view()),
    path("movies/<str:movie_name>/", MovieDetailView.as_view()),
    path('film/<int:film_id>/', FilmView.as_view()),
]
