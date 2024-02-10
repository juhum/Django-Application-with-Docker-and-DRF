from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Task
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword123.')
        # Create a token for the user
        self.token = Token.objects.create(user=self.user)
        # Set the token in the client's Authorization header for authentication
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_category(self):
        response = self.client.post('/api/v1/category/', {'name': 'Work'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Work')

    def test_read_categories(self):
        Category.objects.create(name='Work')
        Category.objects.create(name='Personal')
        response = self.client.get('/api/v1/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_read_category(self):
        category = Category.objects.create(name='Work')
        response = self.client.get(f'/api/v1/category/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Work')

    def test_update_category(self):
        category = Category.objects.create(name='Work')
        response = self.client.put(f'/api/v1/category/{category.id}/', {'name': 'Personal'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.get(id=category.id).name, 'Personal')

    def test_delete_category(self):
        category = Category.objects.create(name='Work')
        response = self.client.delete(f'/api/v1/category/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_create_task(self):
        category = Category.objects.create(name='Work')
        response = self.client.post('/api/v1/tasks/', {'title': 'Do homework', 'category': category.id, 'description': 'asap'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Do homework')

    def test_read_tasks(self):
        Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        Task.objects.create(title='Task 2', category=Category.objects.create(name='Personal'))
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_read_task(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.get(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')

    def test_update_task(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.put(f'/api/v1/tasks/{task.id}/', {'title': 'Updated Task', 'description': 'Updated Description', 'category': task.category.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.delete(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class APITestCaseNoAuth(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_category_no_auth(self):
        response = self.client.post('/api/v1/category/', {'name': 'Work'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_categories_no_auth(self):
        response = self.client.get('/api/v1/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_category_no_auth(self):
        category = Category.objects.create(name='Work')
        response = self.client.get(f'/api/v1/category/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category_no_auth(self):
        category = Category.objects.create(name='Work')
        response = self.client.put(f'/api/v1/category/{category.id}/', {'name': 'Personal'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_category_no_auth(self):
        category = Category.objects.create(name='Work')
        response = self.client.delete(f'/api/v1/category/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_no_auth(self):
        category = Category.objects.create(name='Work')
        response = self.client.post('/api/v1/tasks/', {'title': 'Do homework', 'category': category.id, 'description': 'asap'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_tasks_no_auth(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_task_no_auth(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.get(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_task_no_auth(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.put(f'/api/v1/tasks/{task.id}/', {'title': 'Updated Task', 'description': 'Updated Description', 'category': task.category.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_task_no_auth(self):
        task = Task.objects.create(title='Task 1', category=Category.objects.create(name='Work'))
        response = self.client.delete(f'/api/v1/tasks/{task.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
