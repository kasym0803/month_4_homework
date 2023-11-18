from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    release_data = models.DateField(auto_now_add=True)


