from django.urls import path
from movies.views import MovieView, MainPageView, MovieDetailView


urlpatterns = [
    path('', MovieView.as_view()),
    path("movies/", MainPageView.as_view()),
    path("movies/<str:movie_name>/", MovieDetailView.as_view()),
]
