from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductReviewerializer
from .models import ProductReview

class ProductReviewView(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewerializer