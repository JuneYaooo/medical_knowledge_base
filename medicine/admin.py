from django.contrib import admin
from .models import General, Brand

class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'medical_type', 'name_en', 'indications')
    list_filter = ('medical_type',)
    search_fields = ('name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand_cn', 'common_drug', 'dose', 'usage')
    list_filter = ('common_drug',)
    search_fields = ('brand_cn',)

# class MedicineTypeAdmin(admin.ModelAdmin):
#     list_display = ('medical_type_id', 'name')
#
# class DiseaseAdmin(admin.ModelAdmin):
#     list_display = ('name',)

admin.site.register(General, GeneralAdmin)
admin.site.register(Brand, BrandAdmin)
# admin.site.register(Disease, DiseaseAdmin)
