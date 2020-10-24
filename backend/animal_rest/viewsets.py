from rest_framework import viewsets
from .serializers import AnimalPictureSerializer
from animal.models import Animal_Picture

class UploadImageViewSet(viewsets.ModelViewSet):
    queryset = Animal_Picture.objects.all()
    serializer_class = AnimalPictureSerializer