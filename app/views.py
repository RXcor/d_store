from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import json


from app.models import Product, Position, Basket
from app.serializers import ProductsSerializer, PositionsSerializer, PositionPostSerializer, BasketsSerializer, BasketSerializer, PositionPutSerializer


class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

class Positions(APIView):
    permisson_classes = [permissions.IsAuthenticated,]
    #permission_classes = [permissions.AllowAny,]
    def get(self, request):
        positions = Position.objects.all()
        serializer = PositionsSerializer(positions, many=True)
        return Response(serializer.data)
    def post(self, request):
        position = PositionPostSerializer(data = request.data)
        if position.is_valid():
            position.save()
            return Response({'status': 200})
        else:
            return Response({'status': 400})
    def put(self, request):
        data = request.data
        position = Position.objects.get(id=data.get('position'))
        serializer = PositionPutSerializer(position, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200})
        else:
            return Response({'status': 400})


    def delete(self, request):
        position = Position.objects.get(id=request.data.get('position'))

        if position.delete():
            return Response({'status': 200})
        else:
            return Response({'status': 400})


class Baskets(APIView):
    permission_classes = [permissions.AllowAny,]
    def get(self, request):
        if request.user.role.title == 'manager':
            baskets = Basket.objects.all()
            serializer = BasketsSerializer(baskets, many=True)
            return Response({'data': serializer.data})
        elif request.user.role.title == 'customer':
            basket, created = Basket.objects.get_or_create(customer = request.user.id, active = True)
            serializer = BasketSerializer(basket)
            return Response({'data': serializer.data})
