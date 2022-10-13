from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

class Student(models.Model):
    Student_id = models.BigAutoField(primary_key=True)
    Student_name = models.CharField(max_length=200)
    Student_age = models.IntegerField(default=18)

    #for displaying the actual text
    def __str__(self):
        return self.Student_name
    

