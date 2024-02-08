from django.test import TestCase
from .models import Category, Task
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name="Work")

    def test_category_creation(self):
        category = Category.objects.get(name="Work")
        self.assertEqual(category.name, "Work")

class TaskModelTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Home")
        Task.objects.create(title="Test Task", description="Test Description", completed=False, category=category)

    def test_task_creation(self):
        task = Task.objects.get(title="Test Task")
        self.assertEqual(task.description, "Test Description")
        self.assertFalse(task.completed)
        self.assertEqual(task.category.name, "Home")

class TaskListViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

class PublicApiTests(APITestCase):
    """Test the publicly available API endpoints"""

    def test_list_categories(self):
        """Test retrieving a list of categories"""
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_tasks(self):
        """Test retrieving a list of tasks"""
        response = self.client.get(reverse('task-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PrivateApiTests(APITestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)

    def test_create_task(self):
        """Test creating a new task with authenticated user"""
        category = Category.objects.create(name="Home")
        payload = {'title': 'Test Task', 'description': 'Test task description', 'category': category.id}
        response = self.client.post(reverse('task_create'), payload)

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')


