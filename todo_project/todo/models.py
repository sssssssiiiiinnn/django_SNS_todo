from django.db import models

# Create your models here.
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


class ToDoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    due_date = models.DateField()

    def __str__(self):
        return self.title
