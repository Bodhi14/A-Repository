from django.db import models

class Answer(models.Model):
    ans1 = models.CharField(max_length=300, null=True)
    ans2 = models.CharField(max_length=300, null=True)
    ans3 = models.CharField(max_length=300, null=True)
    ans4 = models.CharField(max_length=300, null=True)


        


