from django.db import models


class User(models.Model):
    iduser = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
