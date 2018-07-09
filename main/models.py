from django.db import models

# Create your models here.


class AddWords(models.Model):
    ID = models.IntegerField()
    UserID = models.CharField(max_length=250)
    Word = models.CharField(max_length=250)
    Pronunciation = models.CharField(max_length=250)
    Phrase = models.CharField(max_length=250)
    Hint = models.CharField(max_length=250)
    Definition = models.CharField(max_length=500)
    Synonym = models.CharField(max_length=250)
    Is_ShareOnline = models.CharField(max_length=250)
    Is_Favourite = models.CharField(max_length=250)
    IsSkip = models.CharField(max_length=250)
    Appearance = models.CharField(max_length=250)
    WAppreance = models.CharField(max_length=250)
    Score = models.IntegerField()
    Addition_Info = models.CharField(max_length=250)
