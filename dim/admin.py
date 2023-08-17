from django.contrib import admin
from .models import MedicineType

class MedicineTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'drug_type')
    search_fields = ('drug_type',)

admin.site.register(MedicineType, MedicineTypeAdmin)