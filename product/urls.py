from django.urls import include, path
from rest_framework.routers import SimpleRouter

from product.views import CategoryListView, ProductViewSet, SimilarProductViewSet

router = SimpleRouter()
router.register('product', ProductViewSet)
router.register('similarproduct', SimilarProductViewSet)
router.register('category', CategoryListView)


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('', include(router.urls))
]