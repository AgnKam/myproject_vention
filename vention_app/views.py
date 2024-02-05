from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import permissions

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

