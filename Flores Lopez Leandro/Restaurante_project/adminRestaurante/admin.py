from django.contrib import admin
from adminRestaurante.models import Mesa
from adminRestaurante.models import Empleado
from adminRestaurante.models import Cliente
from adminRestaurante.models import Pedido
from adminRestaurante.models import Plato

admin.site.register(Mesa)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Plato)