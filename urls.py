from django.urls import path
from .api import stockmarketApi,stockmarketCreateApi,stockmarketUpdateApi,stockmarketDeleteApi
from . import views
urlpatterns = [
    path('api/create', stockmarketCreateApi.as_view()),
    path('api', stockmarketApi.as_view()),
    path('api/<int:pk>', stockmarketUpdateApi.as_view()),
    path('api/<int:pk>/delete', stockmarketDeleteApi.as_view()),
    path('api/predict', views.call_model.as_view())
]