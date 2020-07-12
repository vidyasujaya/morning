from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.decorators import api_view 
from rest_framework import viewsets, permissions
from .permissions import IsOwner

from .models import Task, Category
from .serializers import TaskSerializer, UserSerializer, CategorySerializer
# Create your views here.

class TasksViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

class UserViewSet(viewsets.ReadOnlyModelViewSet):

    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
