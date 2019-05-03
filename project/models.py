from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

def get_image_filename(instance, filename):
    title = instance.project.title
    slug = slugify(title)
    return "./project/static/project/Images/project_images/%s-%s" % (slug, filename)
class Category(models.Model):
    name = models.CharField(max_length=100 )


class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    total_target = models.BigIntegerField(null=True)
    featured = models.BooleanField(default=False)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    project = models.ForeignKey(Project , on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)



class Images(models.Model):
    project = models.ForeignKey(Project, default=None,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name='Image')


class Report_comment (models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)




class Report_project(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Donation(models.Model):
    donation =models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)

class Rate(models.Model):
    rate= models.IntegerField()
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

