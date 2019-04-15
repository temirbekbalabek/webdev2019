from django.db import models

# Create your models here.
class TaskList(models.Model):
    name = models.CharField(max_length=200)
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
    def to_json(self):
        return{
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'due_on': self.due_on,
            'status': self.status,
        }