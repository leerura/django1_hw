from django.db import models

# Create your models here.

class Diary(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=20)
    pub_update = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="diary/", blank=True, null=True) #blank랑 null은 비어있어도 되게 만들어줌

    def __str__(self):
        return self.title
