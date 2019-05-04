from django.db import models
from django.contrib.auth.models import User
from crowdFunding import settings

from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100,blank=True)
    last_name = models.CharField(max_length=100,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    birth_date = models.DateField(default='2001-12-30')
    country = models.CharField(max_length=100,blank=True)
    photo = models.ImageField(upload_to='profile_images',blank=True,default="default.jpeg")
    facebook_profile = models.CharField(max_length=100,blank=True)
   
    def __str__(self):
        return '{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        if photo.height > 300 or photo.width > 300:
            output_size = (300, 300)
            photo.thumbnail(output_size)
            photo.save(self.photo.path)
