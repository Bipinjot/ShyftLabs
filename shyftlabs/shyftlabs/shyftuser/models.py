from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# Create your models here.
class ShyftUser(models.Model):
    '''
    Model: User
    '''
    REQUIRED_FIELDS = ['shyft_email', 'shyft_name', 'shyft_familyname', 'shyft_dob', ]
    USERNAME_FIELD = 'shyft_email'
    shyft_firebaseid = models.CharField(max_length=100)
    shyft_name = models.CharField(max_length=100)
    shyft_familyname = models.CharField(max_length=100)
    shyft_email = models.CharField(max_length=100, unique=True)
    shyft_updatedOn = models.DateTimeField(auto_now=True)
    shyft_userCreatedOn = models.DateTimeField(auto_now_add=True)
    shyft_photoUrl = models.CharField(max_length=500, default="NA")
    shyft_dob = models.DateTimeField(blank=True, null=True)
    isdeleted = models.BooleanField(default=False)
    shyft_usertype = models.CharField(max_length=10, default="Student")
    is_active = models.BooleanField(default=True)
    password = models.CharField(blank=True, max_length=100, null=True)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(blank=True, null=True)

    is_anonymous = False
    is_authenticated = False
