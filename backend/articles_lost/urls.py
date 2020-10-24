from django.urls import path
from . import views

app_name = "articles_lost"

urlpatterns = [
    path('', views.article_list, name="article_list"),
    path('create/', views.article_create, name="article_create"),
    path('update/<int:article_pk>/', views.article_update, name="article_update"),
    path('<int:article_pk>/', views.article_read, name="article_read"),
    path('delete/<int:article_pk>/', views.article_delete, name="article_delete"),
    path('comment/create/<int:article_pk>/', views.comment_create, name="comment_create"),
    path('comment/update/<int:article_pk>/<int:comment_pk>/', views.comment_update, name="comment_update"),
    path('comment/delete/<int:article_pk>/<int:comment_pk>/', views.comment_delete, name="comment_delete"),
    path('search/', views.article_search, name="article_search"),
]