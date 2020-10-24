from articles_lost.models import City, Species, Borough, Animal
from articles_lost.serializers import CitySerializer, SpeciesSerializer, BoroughSerializer, AnimalSerializer
from .serializers import MyArticlesSerializer, SpeciesListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from articles_find.models import Article as article_find
from articles_find.serializers import ArticleFindListSerializer

@swagger_auto_schema()
@api_view(['GET'])
def city_list(request):
    """
        시 목록 제공
    """
    city = City.objects.all()
    serializer = CitySerializer(instance=city, many=True)
    return Response(serializer.data)

@swagger_auto_schema()
@api_view(['GET'])
def species_list(request, animal_pk):
    """
        선택된 동물의 종 목록 제공
    """
    # animal2 = get_object_or_404(Animal, kind=animal)
    # animal_pk = animal2.pk
    species = Species.objects.filter(animal_id=animal_pk)
    serializer = SpeciesListSerializer(instance=species, many=True)
    return Response(serializer.data)

@swagger_auto_schema()
@api_view(['GET'])
def borough_list(request):
    """
        선택된 시에 속한 구 목록 제공
    """
    borough = Borough.objects.all()
    serializer = BoroughSerializer(instance=borough, many=True)
    return Response(serializer.data)

@swagger_auto_schema()
@api_view(['GET'])
def animal_list(request):
    """
        동물 목록 제공
    """
    animal = Animal.objects.all()
    serializer = AnimalSerializer(instance=animal, many=True)
    return Response(serializer.data)
    
@api_view(['POST'])
def search_api(request):
    import requests
    from xml.etree import ElementTree
    url = request.data['url']
    response = requests.get(url)
    root_element = ElementTree.fromstring(response.text)
    animals = []
    iter_element = root_element.iter(tag="item")
    for element in iter_element:
        animal = {}
        animal['thumbnail'] = element.find("filename").text
        animal['find_date'] = element.find("happenDt").text
        animal['find_place'] = element.find("happenPlace").text
        animal['kind'] = element.find("kindCd").text
        animal['color'] = element.find("colorCd").text
        animal['age'] = element.find("age").text
        animal['weight'] = element.find("weight").text
        animal['image_path'] = element.find("popfile").text
        animal['sex'] = element.find('sexCd').text
        animal['neuter'] = element.find("neuterYn").text
        animal['characteristic'] = element.find("specialMark").text
        animal['careplace'] = element.find("careNm").text
        animal['caretel'] = element.find("careTel").text
        animal['careaddress'] = element.find("careAddr").text
        animal['desertionno'] = element.find("desertionNo").text
        animals.append(animal)
    cnt = root_element.find("totalCount")
    return JsonResponse({'animals':animals,'cnt':cnt})

@swagger_auto_schema()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def article_list(request):
    serializer = MyArticlesSerializer(request.user)
    return Response(serializer.data)
