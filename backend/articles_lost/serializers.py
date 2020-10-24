from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment, Animal, Species, City, Borough

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class SpeciesSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer()
    class Meta:
        model = Species
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class BoroughSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    class Meta:
        model = Borough
        fields = '__all__'

class ArticleLostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    animal = AnimalSerializer(required=False)
    species = SpeciesSerializer(required=False)
    city = CitySerializer(required=False)
    borough = BoroughSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleLostListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    animal = AnimalSerializer()
    species = SpeciesSerializer()
    city = CitySerializer()
    borough = BoroughSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class CommentLostSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleLostSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentLostListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class ArticleLostDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    animal = AnimalSerializer()
    species = SpeciesSerializer()
    city = CitySerializer()
    borough = BoroughSerializer()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = '__all__'

    def get_comments(self, article):
        comments = Comment.objects.filter(article=article).order_by('-created_at')
        serializer = CommentLostListSerializer(instance=comments, many=True)
        return serializer.data

class ArticleLostSearchSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    borough = serializers.CharField(max_length=100)
    animal = serializers.CharField(max_length=100)