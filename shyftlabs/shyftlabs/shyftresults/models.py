from django.db import models

# Create your models here.
class ShyftResults(models.Model):
    shyftresult_course = models.ForeignKey(
        'shyftcourse.ShyftCourse', on_delete=models.CASCADE)
    shyftresult_user = models.ForeignKey(
        'shyftuser.ShyftUser', on_delete=models.CASCADE, default=None, null=True)
    shyftresult_score = models.CharField(max_length=1, default='A')
    isdeleted = models.BooleanField(default=False)