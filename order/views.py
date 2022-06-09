from django.shortcuts import render
from rest_framework import generics

from order.models import ProductItem
from order.serializers import OrderSerializer


class OrderAPIView(generics.ListCreateAPIView):
    queryset = ProductItem.objects.all()
    serializer_class = OrderSerializer
