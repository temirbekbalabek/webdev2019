from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TaskListManager(models.Manager):
    def for_user_order_by_name(self, user):
        return self.filter(created_by=user).order_by('name')

class TaskList(models.Model):
    name = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = TaskListManager()
    class Meta:
        verbose_name = 'TaskList'
        verbose_name_plural = 'TaskLists'
    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
        }

class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateField()
    due_on = models.DateField()
    status = models.CharField(max_length=200)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    objects = TaskListManager()
    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
        }