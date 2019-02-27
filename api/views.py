from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from jobs.models import Job
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = BookSerializer