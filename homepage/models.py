from django.db import models


class Video(models.Model):
    text = models.TextField(blank=False, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
