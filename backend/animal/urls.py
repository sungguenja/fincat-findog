from django.urls import path
from . import views

app_name = 'animal'

urlpatterns = [
    path('tf/<int:picture_pk>/', views.what_is_this, name='what_is_this')
]
