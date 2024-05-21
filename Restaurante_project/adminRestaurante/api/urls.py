from rest_framework.routers import DefaultRouter
from adminRestaurante.api.views import MesaViewSet
from adminRestaurante.api.views import EmpleadoViewSet
from adminRestaurante.api.views import ClienteViewSet
from adminRestaurante.api.views import PedidoViewSet
from adminRestaurante.api.views import PlatoViewSet

router = DefaultRouter()
router.register('mesas', MesaViewSet, basename='mesa')
router.register('empleados', EmpleadoViewSet, basename='empleado')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('pedidos', PedidoViewSet, basename='pedido')
router.register('platos', PlatoViewSet, basename='plato')

urlpatterns = router.urls
