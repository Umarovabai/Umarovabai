
from rest_framework import serializers

from cart.models import Cart


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('__all__')
