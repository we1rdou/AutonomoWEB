from rest_framework import viewsets
from adminRestaurante.models import Mesa
from adminRestaurante.api.serializer import MesaSerializer
from adminRestaurante.models import Empleado
from adminRestaurante.api.serializer import EmpleadoSerializer
from adminRestaurante.models import Cliente
from adminRestaurante.api.serializer import ClienteSerializer
from adminRestaurante.models import Pedido
from adminRestaurante.api.serializer import PedidoSerializer
from adminRestaurante.models import Plato
from adminRestaurante.api.serializer import PlatoSerializer

class MesaViewSet(viewsets.ModelViewSet):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PlatoViewSet(viewsets.ModelViewSet):
    queryset = Plato.objects.all()
    serializer_class = PlatoSerializer