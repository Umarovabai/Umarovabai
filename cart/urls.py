from django.urls import path

from cart.views import cart

urlpatterns = [

    path('cart1/', cart, name='cart'),
    # path('order/', OrderAPIView.as_view()),

]
