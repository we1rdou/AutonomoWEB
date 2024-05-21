# tests.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from adminRestaurante.models import Mesa, Empleado, Cliente, Pedido, Plato

class MesaTests(APITestCase):
    def setUp(self):
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

# Repite las pruebas para Cliente, Pedido y Plato de manera similar
