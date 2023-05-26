from django.db import models

# Create your models here.
class ShyftCourse(models.Model):
    '''
    Model: Course
    '''
    shyft_coursename = models.CharField(max_length=100)
    isdeleted = models.BooleanField(default=False)