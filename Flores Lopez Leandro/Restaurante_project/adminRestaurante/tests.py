from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from adminRestaurante.models import Mesa, Empleado, Cliente, Pedido, Plato
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class MesaTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.mesa_data = {'capacidad': 4, 'estado': 'Disponible', 'ubicacion': 'Patio'}
        self.mesa = Mesa.objects.create(**self.mesa_data)
        self.url = reverse('mesa-list')

    def test_create_mesa(self):
        response = self.client.post(self.url, self.mesa_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mesa.objects.count(), 2)

    def test_list_mesas(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_mesa(self):
        url = reverse('mesa-detail', args=[self.mesa.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['ubicacion'], self.mesa.ubicacion)

    def test_update_mesa(self):
        url = reverse('mesa-detail', args=[self.mesa.id])
        updated_data = {'capacidad': 4, 'estado': 'Ocupado', 'ubicacion': 'Interior'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.mesa.refresh_from_db()
        self.assertEqual(self.mesa.estado, 'Ocupado')

    def test_delete_mesa(self):
        url = reverse('mesa-detail', args=[self.mesa.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mesa.objects.count(), 0)

class EmpleadoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.empleado_data = {'nombre': 'John', 'apellido': 'Doe', 'telefono': '123456789', 'correo': 'john@example.com'}
        self.empleado = Empleado.objects.create(**self.empleado_data)
        self.url = reverse('empleado-list')

    def test_create_empleado(self):
        response = self.client.post(self.url, self.empleado_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Empleado.objects.count(), 2)

    def test_list_empleados(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_empleado(self):
        url = reverse('empleado-detail', args=[self.empleado.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.empleado.nombre)

    def test_update_empleado(self):
        url = reverse('empleado-detail', args=[self.empleado.id])
        updated_data = {'nombre': 'Jane', 'apellido': 'Doe', 'telefono': '987654321', 'correo': 'jane@example.com'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.empleado.refresh_from_db()
        self.assertEqual(self.empleado.nombre, 'Jane')

    def test_delete_empleado(self):
        url = reverse('empleado-detail', args=[self.empleado.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Empleado.objects.count(), 0)

class ClienteTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.cliente_data = {'nombre': 'Jane', 'apellido': 'Doe', 'telefono': '123456789', 'correo': 'jane@example.com'}
        self.cliente = Cliente.objects.create(**self.cliente_data)
        self.url = reverse('cliente-list')

    def test_create_cliente(self):
        response = self.client.post(self.url, self.cliente_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cliente.objects.count(), 2)

    def test_list_clientes(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.cliente.nombre)

    def test_update_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id])
        updated_data = {'nombre': 'Janet', 'apellido': 'Doe', 'telefono': '987654321', 'correo': 'janet@example.com'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cliente.refresh_from_db()
        self.assertEqual(self.cliente.nombre, 'Janet')

    def test_delete_cliente(self):
        url = reverse('cliente-detail', args=[self.cliente.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Cliente.objects.count(), 0)

class PedidoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.empleado = Empleado.objects.create(nombre='John', apellido='Doe', telefono='123456789', correo='john@example.com')
        self.cliente = Cliente.objects.create(nombre='Jane', apellido='Doe', telefono='123456789', correo='jane@example.com')
        self.mesa = Mesa.objects.create(capacidad=4, estado='Disponible', ubicacion='Patio')
        self.pedido_data = {'empleado': self.empleado.id, 'cliente': self.cliente.id, 'mesa': self.mesa.id, 'estado': 'Pendiente'}
        self.pedido = Pedido.objects.create(empleado=self.empleado, cliente=self.cliente, mesa=self.mesa, estado='Pendiente')
        self.url = reverse('pedido-list')

    def test_create_pedido(self):
        response = self.client.post(self.url, self.pedido_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pedido.objects.count(), 2)

    def test_list_pedidos(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['estado'], self.pedido.estado)

    def test_update_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id])
        updated_data = {'empleado': self.empleado.id, 'cliente': self.cliente.id, 'mesa': self.mesa.id, 'estado': 'Completado'}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.pedido.refresh_from_db()
        self.assertEqual(self.pedido.estado, 'Completado')

    def test_delete_pedido(self):
        url = reverse('pedido-detail', args=[self.pedido.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Pedido.objects.count(), 0)

class PlatoTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.empleado = Empleado.objects.create(nombre='John', apellido='Doe', telefono='123456789', correo='john@example.com')
        self.cliente = Cliente.objects.create(nombre='Jane', apellido='Doe', telefono='123456789', correo='jane@example.com')
        self.mesa = Mesa.objects.create(capacidad=4, estado='Disponible', ubicacion='Patio')
        self.pedido = Pedido.objects.create(empleado=self.empleado, cliente=self.cliente, mesa=self.mesa, estado='Pendiente')
        self.plato_data = {'pedido': self.pedido.id, 'nombre': 'Pizza', 'descripcion': 'Delicious pizza', 'precio': 10.99, 'categoria': 'Main', 'disponibilidad': True}
        self.plato = Plato.objects.create(pedido=self.pedido, nombre='Pizza', descripcion='Delicious pizza', precio=10.99, categoria='Main', disponibilidad=True)
        self.url = reverse('plato-list')

    def test_create_plato(self):
        response = self.client.post(self.url, self.plato_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Plato.objects.count(), 2)

    def test_list_platos(self):
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_plato(self):
        url = reverse('plato-detail', args=[self.plato.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.plato.nombre)

    def test_update_plato(self):
        url = reverse('plato-detail', args=[self.plato.id])
        updated_data = {'pedido': self.pedido.id, 'nombre': 'Burger', 'descripcion': 'Juicy burger', 'precio': 8.99, 'categoria': 'Main', 'disponibilidad': True}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.plato.refresh_from_db()
        self.assertEqual(self.plato.nombre, 'Burger')

    def test_delete_plato(self):
        url = reverse('plato-detail', args=[self.plato.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Plato.objects.count(), 0)
