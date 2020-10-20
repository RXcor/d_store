from rest_framework import serializers

from app.models import Product, Position, Basket
from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "name")

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('vendor_code', 'title', 'retail_price')

class PositionsSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    class Meta:
        model = Position
        fields = ('product', 'number', 'amount')

class PositionPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('product', 'number', 'basket')
class PositionPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'number', )

class BasketsSerializer(serializers.ModelSerializer):
    customer = UserSerializer()
    positions = PositionsSerializer(many=True)

    class Meta:
        model = Basket
        fields = ('id', 'customer', 'active', 'positions')

class BasketSerializer(serializers.ModelSerializer):
    positions = PositionsSerializer(many=True)
    customer = UserSerializer()
    class Meta:
        model = Basket
        fields = '__all__'
