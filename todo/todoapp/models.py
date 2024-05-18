from django.db import models

# Create your models here.
class todo(models.Model):
    Name = models.CharField(max_length=200)
    Email = models.EmailField()
    password = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.Name
   
   
