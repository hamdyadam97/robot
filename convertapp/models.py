from django.db import models

# Create your models here.
from gdstorage.storage import GoogleDriveStorage

# Define Google Drive Storage
gd_storage = GoogleDriveStorage()


class ConvertAudio(models.Model):
    link_video = models.CharField(max_length=250)
    link = models.CharField(max_length=220,null=True)
    map_data = models.FileField(upload_to='maps',null=True)
    def __str__(self):
        return format(self.link)