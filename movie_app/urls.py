
from django.urls import path
from .views import movie_details, movie_list, movie_details

urlpatterns = [
    path('my_movie/', movie_list, name='movie-list'),
    path('my_movie/<int:pk>/', movie_details, name='movie-details'),
   
]
 