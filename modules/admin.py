from django.contrib import admin
from .models import EducationalModule

@admin.register(EducationalModule)
class EducationalModuleAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'title', 'description')
    search_fields = ('title',)
    list_filter = ('order_number',)
