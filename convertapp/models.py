from django.db import models

# Create your models here.

class ConvertAudio(models.Model):
    link_video = models.CharField(max_length=250)
    link = models.CharField(max_length=220,null=True)

    def __str__(self):
        return format(self.link)