from django.db import models

class Book(models.Model):
    Id = models.BigAutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Author = models.CharField(max_length=50)
    Edition = models.CharField(max_length=20)

    #for displaying the actual text
    def __str__(self):
        return f"{self.Name},{self.Author},{self.Edition}"
    