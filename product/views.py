from rest_framework import generics
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from product.models import Product, Category
from product.serilaizers import ProductListSerializer, SimilarProductSerializer, CategorySerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer

class SimilarProductViewSet(ModelViewSet):
    def get(self, po):
        request = Product.objects.filter(category=po)
        serializer = SimilarProductSerializer
        return Response(serializer(request, many=True).data)



