from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Category, Task


class CategoryApiTestNoAuth(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="test category")

    def test_category_list_no_auth(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_category_detail_no_auth(self):
        response = self.client.get(f"/api/categories/{self.category.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "test category")

    def test_category_create_no_auth(self):
        data = {
            "name": "test category create"
        }
        response = self.client.post("/api/categories/", data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(Category.objects.filter(name="test category create").exists())

    def test_category_update_no_auth(self):
        data = {
            "name": "test category update"
        }
        response = self.client.put(f"/api/categories/{self.category.id}/", data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(Category.objects.filter(name="test category update").exists())

    def test_category_delete_no_auth(self):
        response = self.client.delete(f"/api/categories/{self.category.id}/")
        self.assertEqual(response.status_code, 401)
        self.assertTrue(Category.objects.filter(id=self.category.id).exists())


class CategoryApiTestAuth(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name="test category")

    def test_category_list_auth(self):
        response = self.client.get("/api/categories/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_category_detail_auth(self):
        response = self.client.get(f"/api/categories/{self.category.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "test category")

    def test_category_create_auth(self):
        data = {
            "name": "test category create"
        }
        response = self.client.post("/api/categories/", data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Category.objects.filter(name="test category create").exists())

    def test_category_update_auth(self):
        data = {
            "name": "test category update"
        }
        response = self.client.put(f"/api/categories/{self.category.id}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.get(id=self.category.id).name, "test category update")

    def test_category_delete_auth(self):
        response = self.client.delete(f"/api/categories/{self.category.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Category.objects.filter(id=self.category.id).exists())


class TaskApiTestNoAuth(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="test category")
        self.task = Task.objects.create(title="test task", description="test task description", completed=False,
                                        category=self.category)

    def test_task_list_no_auth(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_detail_no_auth(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "test task")

    def test_task_create_no_auth(self):
        data = {
            "title": "test task create",
            "description": "new task description",
            "completed": False,
            "category": self.category
        }
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(Task.objects.filter(title="test task create").exists())

    def test_task_update_no_auth(self):
        data = {
            "title": "test task update",
            "description": "updated task descrtiption",
            "completed": True,
            "category": self.category
        }
        response = self.client.put(f"/api/tasks/{self.task.id}/", data)
        self.assertEqual(response.status_code, 401)
        self.assertFalse(Task.objects.filter(title="test task update").exists())

    def test_task_delete_no_auth(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, 401)
        self.assertTrue(Task.objects.filter(id=self.task.id).exists())


class TaskApiTestAuth(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.category = Category.objects.create(name="test category")
        self.task = Task.objects.create(title="test task", description="test task description", completed=False,
                                        category=self.category)

    def test_task_list_auth(self):
        response = self.client.get("/api/tasks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_detail_auth(self):
        response = self.client.get(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], "test task")

    def test_task_create_auth(self):
        data = {
            "title": "test task create",
            "description": "new task description",
            "completed": False,
            "category": self.category.id
        }
        response = self.client.post("/api/tasks/", data)
        self.assertEqual(response.status_code, 201)
        self.assertTrue(Task.objects.filter(title="test task create").exists())

    def test_task_update_auth(self):
        data = {
            "title": "test task update",
            "description": "updated task descrtiption",
            "completed": True,
            "category": self.category.id
        }
        response = self.client.put(f"/api/tasks/{self.task.id}/", data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.get(id=self.task.id).title, 'test task update')
        self.assertEqual(Task.objects.get(id=self.task.id).completed, True)

    def test_task_delete_auth(self):
        response = self.client.delete(f"/api/tasks/{self.task.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())


