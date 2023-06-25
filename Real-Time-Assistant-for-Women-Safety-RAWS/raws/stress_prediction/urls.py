from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='stress_prediction'),
    path('predict_stress',views.prediction_stress,name="prediction_stress"),
]