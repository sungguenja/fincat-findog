from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, Comment
from articles_lost.serializers import AnimalSerializer, SpeciesSerializer, CitySerializer, BoroughSerializer

class ArticleFindSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    animal = AnimalSerializer(required=False)
    species = SpeciesSerializer(required=False)
    city = CitySerializer(required=False)
    borough = BoroughSerializer(required=False)
    class Meta:
        model = Article
        fields = '__all__'

class ArticleFindListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    animal = AnimalSerializer()
    species = SpeciesSerializer()
    city = CitySerializer()
    borough = BoroughSerializer()
    class Meta:
        model = Article
        fields = '__all__'

class CommentFindSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleFindSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentFindListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = '__all__'

class ArticleFindDetailSerializer(serializers.ModelSerializer):
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
        serializer = CommentFindListSerializer(instance=comments, many=True)
        return serializer.data

class ArticleFindSearchSerializer(serializers.Serializer):
    city = serializers.CharField(max_length=100)
    borough = serializers.CharField(max_length=100)
    animal = serializers.CharField(max_length=100)