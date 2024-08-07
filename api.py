from rest_framework import generics
from rest_framework.response import Response
from .serializer import stockmarketSerializer
from .models import stockmarket


class stockmarketCreateApi(generics.CreateAPIView):
    queryset = stockmarket.objects.all()
    serializer_class = stockmarketSerializer


class stockmarketApi(generics.ListAPIView):
    queryset = stockmarket.objects.all()
    serializer_class = stockmarketSerializer


class stockmarketUpdateApi(generics.UpdateAPIView):
    queryset = stockmarket.objects.all()
    serializer_class = stockmarketSerializer


class stockmarketDeleteApi(generics.DestroyAPIView):
    queryset = stockmarket.objects.all()
    serializer_class = stockmarketSerializer

class stockmarketPredictApi():
    queryset = stockmarket.objects.all()
    serializer_class = stockmarketSerializer