from django.shortcuts import render
from rest_framework import viewsets
from .models import Capital
from .serializers import CapitalSerializer
# Create your views here.

class CapitalView(viewsets.ModelViewSet):
    queryset=Capital.objects.all()
    serializer_class=CapitalSerializer