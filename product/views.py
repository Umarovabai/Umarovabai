from rest_framework import generics, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category, About_us, Help, OurAdvantages, PublicOffer, Help_image, News, Slider
from product.serilaizers import SimilarProductSerializer, ProductSerializer, CategorySerializer, AboutUsSerializer, \
    HelpSerializer, OurAdvantagesSerializer, PublicOfferSerializer, Help_imageSerializer, NewsSerializer, \
    ListProductSerializer, SliderSerializers, NoveltiesListSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SimilarProductAPIView(APIView):
    def get(self, po):
        queryset = Product.objects.filter(category=po)
        serializer = SimilarProductSerializer
        return Response(serializer(queryset, many=True).data)

class CategoryAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryAPIViewsPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]

class AboutUsApiView(generics.ListAPIView):
    queryset = About_us.objects.all()
    serializer_class = AboutUsSerializer

@api_view(['GET'])
def Help():
    help_que = Help.objects.all()
    help_ser = HelpSerializer(help_que, many=True).data
    help_image_que = Help_image.objects.all()
    help_image_ser = Help_imageSerializer(help_image_que, many=True).data
    return Response({
        'Help': help_ser,
        'image': help_image_ser
    },
        status=status.HTTP_200_OK)


class OurAdvantagesAPIViewSet(viewsets.ModelViewSet):
    queryset = OurAdvantages.objects.all()[0:4]
    serializer_class = OurAdvantagesSerializer

class PublicOfferAPIView(generics.ListAPIView):
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
class NewsViewSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class ListProductViewSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100

class ListProductAPIView(APIView):
    def get(self, po):
        movie = Product.objects.filter(category=po)
        serializer = ListProductSerializer
        pagination_class = ListProductViewSetPagination
        return Response(serializer(movie, many=True).data)

class NoveltiesListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.filter(novelties=True)
    serializer_class = NoveltiesListSerializer

# Слайдер для главной страницы

class SliderAPIViewSet(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializers

class MainAPIViewsPagination(PageNumberPagination):  # Новинка для главной страницы
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MainNoveltiesAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(novelties=True)[0:4]
    serializer_class = NoveltiesListSerializer
    pagination_class = MainAPIViewsPagination

# Хит продаж список 8шт со статусом 'хит продаж'
class BestsellerAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000

class BestsellerAPIViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(bestseller=True)[0:8]
    serializer_class = NoveltiesListSerializer
    pagination_class = BestsellerAPIViewsPagination

class CollectionAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CollectionAPIViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()[0:4]
    serializer_class = CategorySerializer
    pagination_class = CollectionAPIViewsPagination


# Наши приемущества список 4шт
class OurAdvantagesAPIViewSet(viewsets.ModelViewSet):
    queryset = OurAdvantages.objects.all()[0:4]
    serializer_class = OurAdvantagesSerializer

























