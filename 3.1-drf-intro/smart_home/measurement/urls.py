from django.urls import path

from measurement.views import SensorCreate, SensorUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorCreate.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
]
