from django.db import models

# Create your models here.
class Receipe(models.Model):
    receipe_name = models.CharField(max_length=200)
    receipe_description = models.TextField()
    receipe_category = models.CharField(max_length=50,default='')
    receipe_process = models.CharField(max_length=300)
    receipe_ingredient = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe")
    