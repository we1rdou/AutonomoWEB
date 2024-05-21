from rest_framework import serializers
from adminRestaurante.models import Mesa
from adminRestaurante.models import Empleado
from adminRestaurante.models import Cliente
from adminRestaurante.models import Pedido
from adminRestaurante.models import Plato

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mesa
        fields = '__all__'

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pedido
        fields = '__all__'

class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Plato
        fields = '__all__'