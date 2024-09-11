from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets

from catalog.api.v1.serializers import ProductSerializer

from catalog.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
