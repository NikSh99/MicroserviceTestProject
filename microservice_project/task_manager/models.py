from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='task_manager_users')
    user_permissions = models.ManyToManyField(Permission, related_name='task_manager_users')

class Task(models.Model):
    TASK_STATUS_CHOICES = (
        ('created', 'Created'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
    )

    number = models.IntegerField(unique=True)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='created')

    def __str__(self):
        return f"Task {self.number}, Status: {self.status}"
