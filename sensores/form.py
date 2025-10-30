from django import forms
from sensores.models import Motor, Sensor, SensorMotor, DadosSensor

class MotorForm(forms.ModelForm):
    class Meta:
        model = Motor
        fields = ['Marca', 'Modelo', 'Potencia', 'Descricao']
        labels = {'Marca': 'Marca do motor', 'Modelo': 'Modelo do motor', 'Potencia': 'Potencia do motor', 'Descricao': 'Descricao do motor'}

class SensorForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['Nome', 'Tipo']
        labels = {'Nome': 'Nome do sensor', 'Tipo': 'Tipo de sensor'}

class SensorMotorForm(forms.ModelForm):
    class Meta:
        model = SensorMotor
        fields = ['MotorId', 'SensorId']
        labels = {'MotorId': 'MotorId do sensormotor', 'SensorId': 'SensorId do sensor do sensormotor'}

class DadosSensorForm(forms.ModelForm):
    class Meta:
        model = DadosSensor
        fields = ['MotorId', 'SensorId', 'Valor']
        labels = {'MotorId': 'MotorId dos dados do sensor', 'SensorId': 'SensorId dos dados do sensor', 'Valor': 'Valor de dados do sensor'}
