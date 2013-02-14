from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    datetime = models.DateTimeField()
    title = models.CharField(max_length=70)
    content = models.TextField()
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.title
    
class BlogComment(models.Model):
    datetime = models.DateTimeField()
    content = models.TextField()
    firstName = models.CharField(max_length=35)
    lastName = models.CharField(max_length=35)
    email = models.EmailField()
    belongsTo = models.ForeignKey(BlogPost)