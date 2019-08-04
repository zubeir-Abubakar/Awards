from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Projects(models.Model):
  name=models.CharField(max_length=40)
  image=models.ImageField(upload_to='projects/',default='tech.jpeg')
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  description=models.TextField()
  link=models.CharField(max_length=60,default='site.com')

  def __str__(self):
    return self.name

  def project_save(self):
    self.save()

  def project_delete(self):
    self.delete()

  class Meta:
    ordering=['name']

class Profile(models.Model):
  prof_pic = models.ImageField(upload_to='profile/',default='default-avatar.jpg')
  bio=models.TextField()
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  contact=models.IntegerField()
  name=models.CharField(max_length=60)

  def __str__(self):
    return str(self.contact)

  def profile_save(self):
    self.save()

  def profile_delete(self):
    self.delete()

