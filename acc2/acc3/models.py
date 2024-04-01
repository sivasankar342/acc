from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    is_user= models.BooleanField('Is user', default=False)
    is_dealer = models.BooleanField('Is dealer', default=False)
