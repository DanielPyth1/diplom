from django.test import TestCase
from .models import EducationalModule

class EducationalModuleModelTest(TestCase):
    def setUp(self):
        self.module = EducationalModule.objects.create(
            order_number=1,
            title="Модуль 1",
            description="Описание модуля 1"
        )

    def test_module_creation(self):
        """Тест создания образовательного модуля"""
        self.assertEqual(self.module.title, "Модуль 1")
        self.assertEqual(self.module.description, "Описание модуля 1")
        self.assertEqual(self.module.order_number, 1)

    def test_string_representation(self):
        """Тест строкового представления модели"""
        self.assertEqual(str(self.module), "Модуль 1")
