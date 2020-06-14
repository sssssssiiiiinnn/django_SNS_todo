from django.db import models


# Create your models here.
class BoardModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.CharField(max_length=50)
    images = models.ImageField(
        upload_to='',
        height_field=None,
        width_field=None,
        max_length=None
    )
    good = models.IntegerField()
    read = models.IntegerField()
    read_text = models.CharField(max_length=200)
