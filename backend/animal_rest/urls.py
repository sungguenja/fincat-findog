from django.conf.urls import url, include
from rest_framework import routers
from .viewsets import UploadImageViewSet
from .views import MyFileView

router = routers.DefaultRouter()
router.register('images',UploadImageViewSet, 'images')

urlpatterns = [
    url(r'^upload/$', MyFileView.as_view(), name='file-upload'),
    url(r'^', include(router.urls))
]