from django.urls import path
from . import views

app_name = 'articles'


urlpatterns = [
    path('city/', views.city_list, name='city'),
    path('borough/', views.borough_list, name='borough'),
    path('species/<int:animal_pk>/', views.species_list, name='species'),
    path('animal/', views.animal_list, name='animal'),
    path('myarticles/', views.article_list, name="article_list"),
    path('search_api/',views.search_api, name="search_api"),
]
