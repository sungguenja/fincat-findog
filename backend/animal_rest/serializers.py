from rest_framework import serializers
from animal.models import Animal_Picture

class AnimalPictureSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True)
    class Meta:
        model = Animal_Picture
        fields = ('pk','picture',)