from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# you have to run -> python manage.py makemigrations
#then python manage.py migrate

#CREATE SUPERUSER IN CMD -->   python manage.py createsuperuser

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

