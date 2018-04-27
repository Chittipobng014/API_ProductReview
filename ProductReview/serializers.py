from rest_framework import serializers
from .models import ProductReview

class ProductReviewerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = ('id', 'productID', 'rating', 'comment', 'date', 'reviewer')