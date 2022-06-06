from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from product.views import CategoryListView, ProductViewSet, AboutUsApiView, SimilarProductAPIView, Help, \
    OurAdvantagesAPIViewSet, PublicOfferAPIView

router = routers.DefaultRouter()
router.register('product', ProductViewSet)
router.register('Our', OurAdvantagesAPIViewSet, 'OurAdvantages')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListView.as_view()),
    path('about_as/', AboutUsApiView.as_view()),
    path('Similar/<int:po>', SimilarProductAPIView.as_view()),
    path('api/v1/AboutUs/', AboutUsApiView.as_view()),
    path('api/v1/help/', Help),
    path('api/v1/publicoffer/', PublicOfferAPIView.as_view())

]