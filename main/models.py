from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def is_in_stock(self):
        """Check if the product is in stock."""
        return self.stock > 0
