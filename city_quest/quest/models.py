from django.db import models
from django.utils import timezone

# Create your models here.

class Quest(models.Model):
    name=models.CharField(max_length=30,verbose_name="Название квеста")
    description=models.TextField( )
    task=models.TextField()
    maps=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    implementation=models.BooleanField(default=False)
    start_date=models.DateTimeField()
    end_date=models.DateTimeField()
    check=models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Photo(models.Model):
    questID=models.ForeignKey('Quest')
    name=models.CharField(max_length=50)
    text=models.CharField(max_length=60)
    date=models.DateTimeField()
    def __str__(self):
        return self.text