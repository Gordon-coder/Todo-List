from django.shortcuts import render
from rest_framework import viewsets
from .models import User
from .serializer import UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import hashlib

def sha256(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(('POST',))
def register(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    data = json.loads(request.body.decode())

    if {'username', 'password'} < set(data):
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)
    
    username = data['username']
    password = data['password']
    print(sha256(password))  # Debugging line to check password hash

    user = User(username=username, password_hash=sha256(password))
    user.save()
    return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)

@api_view(('POST',))
def login(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    data = json.loads(request.body.decode())

    if {'username', 'password'} < set(data):
        return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    username = data['username']
    password = data['password']
    print(sha256(password))  # Debugging line to check password hash

    try:
        user = User.objects.get(username=username, password_hash=sha256(password)) 
        response = Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
        response.set_cookie('userid', user.id)
        response.set_cookie('password', password, httponly=True)
        return response
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(('POST',))
def change_password(request):
    if request.method != 'POST':
        return Response({"error": "Invalid method"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    data = json.loads(request.body.decode())
    if {'username', 'old_password', 'new_password'} < set(data):
        return Response({"error": "Username, old password, and new password are required"}, status=status.HTTP_400_BAD_REQUEST)
    username = data['username']
    old_password = data['old_password']
    new_password = data['new_password']

    try:
        user = User.objects.get(username=username, password_hash=sha256(old_password))
        user.password_hash = sha256(new_password)
        user.save()
        return Response({"message": "Password changed successfully"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)