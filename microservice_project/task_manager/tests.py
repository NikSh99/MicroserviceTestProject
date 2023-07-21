from django.test import TestCase
import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from models import Task
from django.contrib.auth.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def authenticated_api_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.mark.django_db
def test_create_task(authenticated_api_client, user):
    url = reverse('task-list')
    data = {'title': 'Test Task', 'description': 'This is a test task'}
    response = authenticated_api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    assert Task.objects.get().title == 'Test Task'

@pytest.mark.django_db
def test_retrieve_task(authenticated_api_client, user):
    task = Task.objects.create(title='Test Task', description='This is a test task')
    url = reverse('task-detail', args=[task.id])
    response = authenticated_api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['title'] == 'Test Task'
    assert response.data['description'] == 'This is a test task'

