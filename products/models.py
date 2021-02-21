from django.db import models

# Add for clean method to add custom validation
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Category(models.Model):

    class meta:
        verbose_name_plural = 'Categories'

    name= models.CharField(max_length=20)
    friendly_name= models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=36)
    name= models.CharField(max_length=75)
    gender=models.CharField(max_length=5, null=True, blank=True)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.name


    def clean(self):
        """
        Show error if the user enters discounts or prices below 0
        """
        if self.price and self.price < 0:
            raise ValidationError(_("Price can't be negative"))
        elif self.rating and self.rating < 0:
            raise ValidationError(_("First Order Discount"
                                    " Value can't be negative"))
