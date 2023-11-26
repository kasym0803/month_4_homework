from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=225)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=50)
    release_data = models.DateField(auto_now_add=True)
    review = models.ForeignKey('post.Review', blank=True, related_name='review_related', on_delete=models.CASCADE)


class Category(models.Model):
    post = models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='category_related')
    text = models.TextField()
    release = models.DateField(auto_now_add=True)


class Review(models.Model):
    product = models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='review_related_name')
    text = models.TextField()
    release = models.DateTimeField(auto_now_add=True)

