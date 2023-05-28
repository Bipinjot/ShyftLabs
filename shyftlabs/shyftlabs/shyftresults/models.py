from django.db import models

# Create your models here.
class ShyftResults(models.Model):
    # shyftresult_course = models.ForeignKey(
    #     'shyftcourse.ShyftCourse', on_delete=models.CASCADE)
    # shyftresult_user = models.ForeignKey(
    #     'shyftuser.ShyftUser', on_delete=models.CASCADE, default=None, null=True)

    shyft_coursename = models.CharField(max_length=100)
    shyft_username = models.CharField(max_length=100)
    shyftresult_score = models.CharField(max_length=1, default='A')
    isdeleted = models.BooleanField(default=False)