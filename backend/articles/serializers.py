from articles_lost.models import Article as Article_lost
from articles_find.models import Article as Article_find
from articles_lost.serializers import ArticleLostListSerializer
from articles_find.serializers import ArticleFindListSerializer
from rest_framework import serializers
from accounts.models import User
from articles_lost.models import Species


class MyArticlesSerializer(serializers.ModelSerializer):
    articles_lost = serializers.SerializerMethodField()
    articles_find = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'nickname', 'email', 'phone_number', 'articles_lost', 'articles_find']

    def get_articles_lost(self, user):
        articles_lost = Article_lost.objects.filter(user=user).order_by('-created_at')
        serializer = ArticleLostListSerializer(instance=articles_lost, many=True)
        return serializer.data

    def get_articles_find(self, user):
        articles_find = Article_find.objects.filter(user=user).order_by('-created_at')
        serializer = ArticleFindListSerializer(instance=articles_find, many=True)
        return serializer.data


class SpeciesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['species']