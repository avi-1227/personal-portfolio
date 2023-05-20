from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    discriptions = models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
