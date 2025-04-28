from django.db import models

# Create your models here.


class Myprojects(models.Model):
    pname=models.CharField(max_length=100)
    pdesc=models.TextField()


    def __str__(self):
        return self.pname
    

class Visiter(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.IntegerField()
    subject=models.TextField()
    message=models.TextField()
