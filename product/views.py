from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from product.models import Product, Category
from product.serilaizers import SimilarProductSerializer, ProductSerializer, CategorySerializer


class ProductAPIViewSet(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SimilarProductViewSet(viewsets.ModelViewSet):
    def get(self, po):
        request = Product.objects.filter(category=po)
        serializer = SimilarProductSerializer
        return Response(serializer(request, many=True).data)

class CategoryAPIViewsPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryAPIViewsPagination
    permission_classes = [IsAuthenticatedOrReadOnly, ]




