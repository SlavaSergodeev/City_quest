from django.db import models
from django.utils import timezone
from quest.models import Quest


# Create your models here.
class Comment(models.Model):
    text = models.TextField(verbose_name="Коментарий")
    date = models.DateTimeField(default=timezone.now(), verbose_name="Дата коментария")
    like = models.IntegerField(default=0, verbose_name="Количесвто лайков")
    quest_id = models.IntegerField(default=0, verbose_name="Идентификатор квеста")
    questID = models.ForeignKey(Quest)

    def __str__(self):
        return self.quest_id
