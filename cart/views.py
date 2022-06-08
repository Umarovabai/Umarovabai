from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from cart.models import Cart
from product.models import Product
from product.serilaizers import SimilarSerializer


@api_view(['GET'])
def cart(request):
    proid = []
    for i in Cart.objects.all():
        # tell=i.objects.get(id=6)
        # uli=tell.product
        print(i)
        str(i)
        proid.append(i)
    cart1 = proid[0]
    cart2 = proid[1]
    cart3 = proid[2]
    # a4 = proid[3]
    # a5 = proid[4]
    ca1 = Product.objects.filter(name=cart1)
    asert = SimilarSerializer(ca1, many=True).data

    ca2 = Product.objects.filter(name=cart2)
    asert2 = SimilarSerializer(ca2, many=True).data
    return Response({
        'Корзина': 'Товары',
        '1': asert,
        '2': asert2

    },
        status=status.HTTP_200_OK)
