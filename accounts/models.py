<<<<<<< HEAD
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
        return f'{self.user.username} Profile'

    def save(self,*args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        photo = Image.open(self.photo.path)
        if photo.height > 300 or photo.width > 300:
            output_size = (300, 300)
            photo.thumbnail(output_size)
            photo.save(self.photo.path)

   
=======
# from django.db import models
#
#
# class User(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=100)
#     phone = models.BigIntegerField()
#     birth_date = models.DateField()
#     country = models.CharField(max_length=100)
#     facebook_profile = models.CharField(max_length=100)
#     photo = models.ImageField(upload_to='user/images/%Y/%m/%d/')
>>>>>>> c1e30cfb0050b6ff6eb3be8c26ba002274d586c9
