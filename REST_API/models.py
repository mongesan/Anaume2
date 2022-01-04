from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField('タイトル', max_length=20)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    # description
    # heart

    def __str__(self):
        return self.title
