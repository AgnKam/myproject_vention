from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, Task
from .serializers import CategorySerializer, TaskSerializer
from rest_framework import permissions
from django.http import HttpResponse
from datetime import datetime, timedelta
from .forms import TaskForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CategoryForm

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

def home(request):
    categories = Category.objects.all()
    recent_tasks = Task.objects.filter(due_date__gte=datetime.now() - timedelta(days=7))  # Example
    return render(request, 'vention_app/home.html', {'categories': categories, 'recent_tasks': recent_tasks})

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')  # Redirect to the task list page
    else:
        form = TaskForm()
    return render(request, 'vention_app/create_task.html', {'form': form})

class TaskListView(ListView):
    model = Task
    template_name = 'vention_app/tasks.html'  # Replace with your template path
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'vention_app/task_create.html'  # Replace with your template path
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'vention_app/task_update.html'
    success_url = reverse_lazy('tasks')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'vention_app/task_confirm_delete.html'
    success_url = reverse_lazy('tasks')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'vention_app/task_list.html', {'tasks': tasks})

class CategoryListView(ListView):
    model = Category
    template_name = 'vention_app/category_list.html'

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'vention_app/category_create.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'vention_app/category_update.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'vention_app/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

