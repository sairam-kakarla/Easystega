from django.db import models

# Create your models here.
class Stega(models.Model):
    username=models.CharField(max_length=150)
    user_key=models.CharField(max_length=30)
    fernet_key=models.CharField(max_length=60)
