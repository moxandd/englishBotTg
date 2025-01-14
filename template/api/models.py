from django.db import models
from ..authentication.models import TemplateUser


class Podcast(models.Model):
    audio_file = models.FileField(upload_to="audio", default=None)
    title = models.CharField(max_length=200, default="Podcast")


class TelegramConversationView(models.Model):
    title = models.CharField(max_length=200, default="Why cars still don't fly?")
    users = models.ManyToManyField(TemplateUser)
    podcasts = models.ManyToManyField(Podcast)
    created_at = models.DateTimeField(auto_now_add=True)
