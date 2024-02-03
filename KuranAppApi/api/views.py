from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status, views, response
from .serializers import UserSerializer

class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return response.Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(views.APIView):
    def post(self, request):
        user = authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            login(request, user)
            return response.Response(UserSerializer(user).data)
        return response.Response({'detail': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)