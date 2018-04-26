from django.db import models

class ProductReview(models.Model):
    rating = models.IntegerField()
    comment = models.name = models.CharField(max_length=256)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    productID = models.IntegerField()
