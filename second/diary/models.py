from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=20)
    pub_update = models.DateTimeField()
    body = models.TextField()

    def __str__(self):
        return self.title
