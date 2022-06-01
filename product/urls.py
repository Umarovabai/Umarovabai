from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import SimpleRouter

from product.views import CategoryAPIView, ProductAPIViewSet

router = routers.DefaultRouter()
# router.register('product', ProductViewSet)
# router.register('category', CategoryListView)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/category/', CategoryAPIView.as_view()),
    path('api/v1/', ProductAPIViewSet.as_view())
]