from django.db import models

# Create your models here.
class ENotice(models.Model):
    Topic= models.CharField(max_length=800)
    Name= models.CharField(max_length=400)
    File=models.FileField(upload_to='media')
    Disc = models.TextField()
    def __str__(self):
        return self.Name