from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    body=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='posts/',default="")

    def __str__(self):
        return self.title[0:20]
