from django.urls import path, include
from rest_framework import routers
from catalog.api.v1.views import ProductViewSet

app_name = 'catalog'

router = routers.DefaultRouter()
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]