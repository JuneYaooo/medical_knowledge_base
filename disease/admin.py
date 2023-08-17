from django.contrib import admin
from .models import Common

class CommonAdmin(admin.ModelAdmin):
    list_display = ('id', 'disease_name', 'department_name')
    search_fields = ('disease_name', 'department_name')

admin.site.register(Common, CommonAdmin)
