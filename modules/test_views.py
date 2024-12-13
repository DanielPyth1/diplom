from rest_framework.test import APITestCase
from rest_framework import status
from .models import EducationalModule

class EducationalModuleAPITest(APITestCase):
    def setUp(self):
        self.module = EducationalModule.objects.create(
            order_number=1,
            title="Модуль 1",
            description="Описание модуля 1"
        )
        self.module_url = "/api/modules/"

    def test_get_modules(self):
        """Тест получения списка модулей"""
        response = self.client.get(self.module_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Модуль 1")

    def test_create_module(self):
        """Тест создания модуля"""
        data = {
            "order_number": 2,
            "title": "Модуль 2",
            "description": "Описание модуля 2"
        }
        response = self.client.post(self.module_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EducationalModule.objects.count(), 2)

    def test_update_module(self):
        """Тест обновления модуля"""
        data = {
            "order_number": 1,
            "title": "Обновленный модуль",
            "description": "Обновленное описание"
        }
        response = self.client.put(f"{self.module_url}{self.module.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.module.refresh_from_db()
        self.assertEqual(self.module.title, "Обновленный модуль")

    def test_delete_module(self):
        """Тест удаления модуля"""
        response = self.client.delete(f"{self.module_url}{self.module.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EducationalModule.objects.count(), 0)
