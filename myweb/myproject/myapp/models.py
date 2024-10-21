from django.db import models

# Create your models here.
class data(models.Model):
    full_name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    address=models.CharField(max_length=150)