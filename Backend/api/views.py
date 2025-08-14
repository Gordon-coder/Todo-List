from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(('POST',))
def register(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    username = request.POST.get('username')
    password = request.POST.get('password}_hash')
    if not (username and password):
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = User(username=username, password_hash=password)
    user.save()
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

@api_view(('POST',))
def login(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    username = request.POST.get('username')
    password = request.POST.get('password_hash')
    if not (username and password):
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username, password_hash=password)
        return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(('POST',))
def change_password(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    username = request.POST.get('username')
    old_password = request.POST.get('old_password_hash')
    new_password = request.POST.get('new_password_hash')

    if not (username and old_password and new_password):
        return Response({"error": "Username, old password, and new password are required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username, password_hash=old_password)
        user.password_hash = new_password
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)