from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, viewsets


from app.models import CustomUser
from app.serializers import CustomUserSerializer


class CustomUserViewSet(ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        CustomUser.objects.create_user(serializer)
        return Response(data=serializer.data, status=HTTP_200_OK)
# Create your views here.
