from django.db import models

# Create your models here.

class Student(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    Roll = models.IntegerField()
    Image = models.ImageField(upload_to = 'images/')
