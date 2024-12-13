from django.db import models

class EducationalModule(models.Model):
    order_number = models.PositiveIntegerField(verbose_name="Порядковый номер")
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Образовательный модуль"
        verbose_name_plural = "Образовательные модули"
        ordering = ['order_number']

    def __str__(self):
        return self.title
