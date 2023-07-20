from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField(max_length=250)

    def __str__(self):
        return self.name

class team(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pics')
    designation=models.CharField(max_length=25)

    def __str__(self):
        return self.name
