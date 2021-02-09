from django.db import models


class Category(models.Model):
    
    class meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Products(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=36)
    name= models.CharField(max_length=75)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name