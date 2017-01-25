from django.db import models
from django.contrib.auth.models import User


# Create your models here.
CHOSE_DIR=(('jj','jj'),('dhd','dhd'),('dsd','dsd'),('bld','bld'),('syd','syd'),('syad','syad'),('nhd','nhd'),('xhd','xhd'))
class UserProfile(models.Model):
    belong_to = models.OneToOneField(to=User,related_name='profile')
    profile_image = models.ImageField(upload_to='User',null=True,blank=True)
    gender = models.CharField(null=True,blank=True,choices=(('male','male'),('female','female')),max_length=10)
    def __str__(self):
        return str(self.belong_to)

class Road(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    gender = models.CharField(null=True,blank=True,choices=CHOSE_DIR,max_length=200)
    def __str__(self):
        return self.name

class Domain(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    biography = models.TextField(null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    component = models.TextField(null=True,blank=True)
    product = models.TextField(null=True,blank=True)
    scenic = models.TextField(null=True,blank=True)
    family = models.TextField(null=True,blank=True)
    photo = models.ImageField('upload',upload_to='domain',null=True,blank=True)
    photo_add = models.ImageField('upload_add',upload_to='domain_add',null=True,blank=True)
    photo_add_b = models.ImageField('upload_add_b',upload_to='domain_add',null=True,blank=True)
    gender = models.CharField(null=True,blank=True,choices=CHOSE_DIR,max_length=200)
    salary = models.CharField(null=True,blank=True,max_length=200)
    belong_to = models.ForeignKey(to=Road,related_name='vassal',null=True,blank=True)
    def __str__(self):
        return self.name


class Family(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    biography = models.TextField(null=True,blank=True)
    photo = models.ImageField('upload',upload_to='Family',null=True,blank=True)
    gender = models.CharField(null=True,blank=True,choices=CHOSE_DIR,max_length=200)
    salary = models.CharField(null=True,blank=True,max_length=200)
    roads = models.ManyToManyField(Road)
    def __str__(self):
        return self.name

class People(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    biography = models.TextField(null=True,blank=True)
    photo = models.ImageField('upload',upload_to='People',null=True,blank=True)
    native = models.CharField(null=True,blank=True,max_length=200)
    gender = models.CharField(null=True,blank=True,choices=(('male','male'),('female','female'),),max_length=200)
    salary = models.CharField(null=True,blank=True,max_length=200)
    lifetime = models.CharField(null=True,blank=True,max_length=200)
    belong_to = models.ForeignKey(to=Family,related_name='vassal',null=True,blank=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    comment = models.TextField(null=True,blank=True)
    belong_to = models.ForeignKey(to=Domain,related_name='under_comment',null=True,blank=True)
    belong_for = models.ForeignKey(to=User,related_name='under_comment',null=True,blank=True)
    best_comment = models.BooleanField(default=False)
    def __str__(self):
        return self.comment

class Message(models.Model):
    content = models.TextField(null=True,blank=True)
    belong_to = models.ForeignKey(to=User,related_name='under_message',null=True,blank=True)
    def __str__(self):
        return self.content
