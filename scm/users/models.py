from django.db import models


# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=500, unique=True)
    phone_number = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    password = models.CharField(max_length=1000)

    class Meta:
        db_table = "scm_users"
