from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serilizers import StockSerializers
#lists all stocks or crreate a new one
#stocks
class StockList(APIView):
    def get(self,request):
        stocks=Stock.objects.all()
        serilizer=StockSerializers(stocks,many=True)
        return Response(serilizer.data)
    def post(self):
        pass


# Create your views here.
