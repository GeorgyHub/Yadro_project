from django.shortcuts import render
from rest_framework import routers, serializers, viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html')