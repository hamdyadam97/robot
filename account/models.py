from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    first_name = models.CharField(max_length=20,null=True,blank=True)
    last_name = models.CharField(max_length=20,null=True,blank=True)
    mobile = models.CharField(max_length=11,null=True,blank=True)
    address= models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(upload_to='profile',null=True,blank=True)

    def __str__(self):
        return format(self.user.username)