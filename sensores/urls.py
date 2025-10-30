from django.urls import path
from .views import MotorListView, MotorCreateView, MotorUpdateView, MotorDeleteView, SensorListView, SensorCreateView, SensorUpdateView, SensorDeleteView, SensorMotorListView, SensorMotorCreateView, SensorMotorUpdateView, SensorMotorDeleteView, DadosSensorListView, DadosSensorCreateView, DadosSensorUpdateView, DadosSensorDeleteView

urlpatterns = [path('motor/', MotorListView.as_view(), name='motor_list'),
               path('motor/novo/', MotorCreateView.as_view(), name='motor_create'),
               path('motor/<int:pk>/editar/', MotorUpdateView.as_view(), name ='motor_update'),
               path('motor/<int:pk>/delete/', MotorDeleteView.as_view(), name='motor_delete'),

               path('sensores/', SensorListView.as_view(), name='sensor_list'),
               path('sensores/novo/', SensorCreateView.as_view(), name='sensor_create'),
               path('sensores/<int:pk>/editar/', SensorUpdateView.as_view(), name ='sensor_update'),
               path('sensores/<int:pk>/delete/', SensorDeleteView.as_view(), name='sensor_delete'),

               path('sensormotor/', SensorMotorListView.as_view(), name='sensormotor_list'),
               path('sensormotor/novo/', SensorMotorCreateView.as_view(), name='sensormotor_create'),
               path('sensormotor/<int:pk>/editar/', SensorMotorUpdateView.as_view(), name ='sensormotor_update'),
               path('sensormotor/<int:pk>/delete/', SensorMotorDeleteView.as_view(), name='sensormotor_delete'),

               path('dadosSensor/', DadosSensorListView.as_view(), name='dadossensor_list'),
               path('dadossensor/novo/', DadosSensorCreateView.as_view(), name='dadossensor_create'),
               path('dadossensor/<int:pk>/editar/', DadosSensorUpdateView.as_view(), name ='dadossensor_update'),
               path('dadossensor/<int:pk>/delete/', DadosSensorDeleteView.as_view(), name='dadossensor_delete')
               ]