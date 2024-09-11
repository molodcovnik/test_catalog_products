from rest_framework import serializers
from catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', )

    def validate_price(self, value):
        if value >= 0:
            return value
        raise serializers.ValidationError("Цена не может быть отрицательной")
