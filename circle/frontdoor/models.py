from django.db import models
from django.utils import timezone
# Create your models here.
class Circle(models.Model):
    name=models.CharField(max_length=30)
    intro=models.CharField(max_length=100)
    num=models.IntegerField()

class Comment(models.Model):
    circle=models.ForeignKey(Circle, on_delete=models.CASCADE)
    comment=models.CharField(max_length=300)
    time=models.DateTimeField()

    def __str__(self):
        return self.comment

