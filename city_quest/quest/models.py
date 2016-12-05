from django.db import models
from django.utils import timezone

# Create your models here.

class Quest(models.Model):
    name=models.CharField(max_length=30, verbose_name="Название квеста")
    description=models.TextField(verbose_name="Описание квеста")
    task=models.TextField(verbose_name="Задание квеста")
    maps=models.TextField(verbose_name="Карта")
    create_date=models.DateTimeField(default=timezone.now())
    implementation=models.BooleanField(default=False)
    start_date=models.DateTimeField(verbose_name="Дата начала квеста")
    end_date=models.DateTimeField(verbose_name="Дата окончаниея квеста")
    check=models.CharField(max_length=30, verbose_name="Слово проверки прохождения квеста")
    def __str__(self):
        return self.name

    class Meta:
        default_related_name = 'Квесты'
class Photo(models.Model):
    questID=models.ForeignKey('Quest')
    name=models.CharField(max_length=50, verbose_name="Название фото")
    text=models.CharField(max_length=60, verbose_name="Текст")
    date=models.DateTimeField(verbose_name="Дата")
    def __str__(self):
        return self.text

