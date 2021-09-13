from django.urls import path

from . import views

urlpatterns = [
    path('movies/', views.MoviesListView.as_view()),
    path('movies/<uuid:pk>/', views.SingleMovieView.as_view(), name='movie_detail'),
]
