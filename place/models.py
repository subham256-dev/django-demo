from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Place(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    description=models.TextField()
    rating=models.FloatField()  
    image=models.ImageField(upload_to='placeimages')

   
