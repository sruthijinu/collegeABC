from django.db import models

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pictures')


    def __str__(self):
        return self.name
