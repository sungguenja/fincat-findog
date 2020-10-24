from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import ArticleLostSerializer, ArticleLostListSerializer, ArticleLostDetailSerializer, CommentLostSerializer, CommentLostListSerializer, ArticleLostSearchSerializer
from .models import Article, Comment, Animal, Species, City, Borough
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse, HttpResponseForbidden
from drf_yasg.utils import swagger_auto_schema
# Create your views here.

@swagger_auto_schema(method='post', request_body=ArticleLostSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def article_create(request):
    """
        게시글 작성
        {
            animal: str,
            species: str,
            city: str,
            borough: str,
            title: str,
            name: str,
            content: str,
            gender: 'Male' or 'Female' or 'Unknown',
            chip: True or False,
            age: str,
            time: str,
            image_url: str
        }
    """
    city = get_object_or_404(City, city=request.data.get('city'))
    animal = get_object_or_404(Animal, kind=request.data.get('animal'))
    species = get_object_or_404(Species, species=request.data.get('species'), animal_id=animal.id)
    borough = get_object_or_404(Borough, gu=request.data.get('borough'))
    data = {
        'title': request.data.get('title'),
        'name' : request.data.get('name'),
        'content': request.data.get('content'),
        'gender': request.data.get('gender'),
        'chip': request.data.get('chip'),
        'age': request.data.get('age'),
        'time': request.data.get('time'),
        'image_url': request.data.get('image_url'),
    }
    serializer = ArticleLostSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, city=city, animal=animal, species=species, borough=borough)
        return Response(serializer.data)

@swagger_auto_schema(method='put', request_body=ArticleLostSerializer)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def article_update(request, article_pk):
    """
        게시글 업데이트
        {
            animal: str,
            species: str,
            city: str,
            borough: str,
            title: str,
            name: str,
            content: str,
            gender: 'Male' or 'Female' or 'Unknown',
            chip: True or False,
            age: str,
            time: str,
            image_url: str
        }
    """
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        if request.method == 'GET':
            serializer = ArticleLostSerializer(article)
            return Response(serializer.data)
        else:
            data = {
            'title': request.data.get('title', article.title),
            'name' : request.data.get('name', article.name),
            'content': request.data.get('content', article.content),
            'gender': request.data.get('gender', article.gender),
            'chip': request.data.get('chip', article.chip),
            'age': request.data.get('age', article.age),
            'time': request.data.get('time', article.time),
            'image_url': request.data.get('image_url', article.image_url),
            }   
            serializer = ArticleLostSerializer(article, data=data)
            city = get_object_or_404(City, city=request.data.get('city'))
            animal = get_object_or_404(Animal, kind=request.data.get('animal'))
            species = get_object_or_404(Species, species=request.data.get('species'), animal_id=animal.id)
            borough = get_object_or_404(Borough, gu=request.data.get('borough'))
            if serializer.is_valid(raise_exception=True):
                serializer.save(city=city, animal=animal, species=species, borough=borough)
                return Response(serializer.data)

@swagger_auto_schema()
@api_view(['GET'])
def article_read(request, article_pk):
    """
        게시글 조회
    """
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleLostDetailSerializer(instance=article)
    return Response(serializer.data)

@swagger_auto_schema(method='delete')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def article_delete(request, article_pk):
    """
        게시글 삭제
    """
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == article.user:
        article.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponseForbidden()

@swagger_auto_schema(method='post', request_body=CommentLostSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    """
        댓글 작성
        {
            content: str,
        }
    """
    article = get_object_or_404(Article, pk=article_pk)
    comment_serializer = CommentLostSerializer(data=request.data)
    if comment_serializer.is_valid(raise_exception=True):
        comment_serializer.save(user=request.user, article=article)
        article_serializer = ArticleLostDetailSerializer(article)
        return Response(article_serializer.data)

@swagger_auto_schema(method='put', request_body=CommentLostSerializer)
@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_update(request, article_pk, comment_pk):
    """
        댓글 업데이트
        {
            content: str,
        }
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        if request.method == 'GET':
            serializer = CommentLostSerializer(comment)
            return Response(serializer.data)
        else:
            data = {
                'content': request.data.get('content', comment.content)
            }
            serializer = CommentLostSerializer(comment, data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
    else:
        return HttpResponseForbidden()

@swagger_auto_schema(method='delete')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_delete(request, article_pk, comment_pk):
    """
        댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.user == comment.user:
        comment.delete()
        article_serializer = ArticleLostDetailSerializer(article)
        return Response(article_serializer.data)
    else:
        return HttpResponseForbidden()

@swagger_auto_schema()
@api_view(['GET'])
def article_list(request):
    """
        전체 게시글 목록 조회
    """
    articles = Article.objects.all().order_by('-created_at')
    serializer = ArticleLostListSerializer(instance=articles, many=True)
    return Response(serializer.data)


@swagger_auto_schema(method='POST', request_body=ArticleLostSearchSerializer)
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def article_search(request):
    """
        검색 조건에 맞는 게시글 목록 제공
        {
            city: "str",
            borough: "str",
            animal: "str",
        }
    """
    if request.data.get('city') and not request.data.get('borough') and not request.data.get('animal'):
        city = get_object_or_404(City, city=request.data.get('city'))
        articles = Article.objects.filter(city_id=city.id).order_by('-created_at')
    elif not request.data.get('city') and request.data.get('borough') and not request.data.get('animal'):
        borough = get_object_or_404(Borough, gu=request.data.get('borough'))
        articles = Article.objects.filter(borough_id=borough.id).order_by('-created_at')
    elif not request.data.get('city') and not request.data.get('borough') and request.data.get('animal'):
        animal = get_object_or_404(Animal, kind=request.data.get('animal'))
        articles = Article.objects.filter(animal_id=animal.id).order_by('-created_at')
    elif request.data.get('city') and request.data.get('borough') and not request.data.get('animal'):
        city = get_object_or_404(City, city=request.data.get('city'))
        borough = get_object_or_404(Borough, gu=request.data.get('borough'))
        articles = Article.objects.filter(borough_id=borough.id).filter(city_id=city.id).order_by('-created_at')
    elif request.data.get('city') and not request.data.get('borough') and request.data.get('animal'):
        city = get_object_or_404(City, city=request.data.get('city'))
        animal = get_object_or_404(Animal, kind=request.data.get('animal'))
        articles = Article.objects.filter(animal_id=animal.id).filter(city_id=city.id).order_by('-created_at')
    elif not request.data.get('city') and request.data.get('borough') and request.data.get('animal'):
        borough = get_object_or_404(Borough, gu=request.data.get('borough'))
        animal = get_object_or_404(Animal, kind=request.data.get('animal'))
        articles = Article.objects.filter(borough_id=borough.id).filter(animal_id=animal.id).order_by('-created_at')
    elif request.data.get('city') and request.data.get('borough') and request.data.get('animal'):
        borough = get_object_or_404(Borough, gu=request.data.get('borough'))
        animal = get_object_or_404(Animal, kind=request.data.get('animal'))
        city = get_object_or_404(City, city=request.data.get('city'))
        articles = Article.objects.filter(borough_id=borough.id).filter(animal_id=animal.id).filter(city_id=city.id).order_by('-created_at')
    else:
        articles = Article.objects.all()
    serializer = ArticleLostListSerializer(instance=articles, many=True)
    return Response(serializer.data)