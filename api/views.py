from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from res_tutorials.models import Books


# Create your views here.
class BookAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
