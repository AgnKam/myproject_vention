from django.test import TestCase
from .models import Category, Task
from django.urls import reverse

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
