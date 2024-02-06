from django.urls import path, include
from .views import (
    CategoryViewSet, TaskViewSet, TaskListView, TaskCreateView,
    TaskUpdateView, TaskDeleteView, home, CategoryListView, 
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # DRF viewsets
    path('', home, name='home'),  # Root URL for your home page

    # Task management URLs
    path('tasks/', TaskListView.as_view(), name='tasks'),  # List tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),  # Create a new task
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),  # Update a task
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),  # Delete a task

    # Category management URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
