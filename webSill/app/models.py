from django.db import models

# Create your models here.


class Collection(models.Model):
    ID = models.IntegerField(primary_key=True)
    IDtype = models.CharField(max_length=50)
    Name = models.CharField(max_length=200)
    Detail= models.CharField(max_length=500)
    Image1 = models.CharField(max_length=200)
    Image2 = models.CharField(max_length=200)
    Linkdownload = models.CharField(max_length=500)