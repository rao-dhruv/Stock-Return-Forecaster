from django.shortcuts import render
from .apps import PredictorConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
    def get(self,request):
        if request.method == 'GET':
            Open = float(request.GET.get('Open'))
            High = float(request.GET.get('High'))
            Low = float(request.GET.get('Low'))
            Close = float(request.GET.get('Close'))
            print(Open, High, Low, Close)
            prediction = PredictorConfig.model.predict([[Open, High, Low, Close]])
            print(prediction[0])
            response = {'returns': prediction[0]}
            return JsonResponse(response)
