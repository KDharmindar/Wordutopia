from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class AddWords(models.Model):
    id = models.BigAutoField(primary_key=True)
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    Word = models.CharField(max_length=250,default='')
    Pronunciation = models.CharField(max_length=250,default='')
    Phrase = models.CharField(max_length=250,default='')
    Hint = models.CharField(max_length=250,default='')
    Definition = models.CharField(max_length=500,default='')
    Synonym = models.CharField(max_length=250,default='')
    Is_ShareOnline = models.CharField(max_length=250,default='')
    Is_Favourite = models.CharField(max_length=250,default='')
    IsSkip = models.CharField(max_length=250,default='')
    Appearance = models.CharField(max_length=250,default='')
    WAppreance = models.CharField(max_length=250,default='')
    Score = models.IntegerField()
    Addition_Info = models.CharField(max_length=250,default='')

class CreateNotes(models.Model):
    Title = models.CharField(max_length=250, default='')
    Content = models.CharField(max_length=500, default='')    