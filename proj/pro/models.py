
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name=models.CharField(max_length=255)
    email=models.CharField(max_length=255, unique=True)
    password=models.CharField(max_length=255)
    username = ""

    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]



class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = models.DateTimeField(default=timezone.now)
    

class WordIndex(models.Model):
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)
    word = models.CharField(max_length=255)
