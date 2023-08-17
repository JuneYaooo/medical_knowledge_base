from django.db import models
from dim.models import MedicineType
from disease.models import Common

class General(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    name = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200, blank=True, null=True)
    department_category = models.CharField(max_length=200, blank=True, null=True)
    medical_insurance_status = models.CharField(max_length=200, blank=True, null=True)
    children_taboo = models.TextField(blank=True, null=True)
    pregnant_women_taboo = models.TextField(blank=True, null=True)
    elderly_taboo = models.TextField(blank=True, null=True)
    indications = models.TextField(blank=True, null=True)
    contraindication = models.TextField(blank=True, null=True)
    adr = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    interaction = models.TextField(blank=True, null=True)
    storage = models.TextField(blank=True, null=True)
    ingredient = models.TextField(blank=True, null=True)
    dosage_form = models.TextField(blank=True, null=True)
    medical_type = models.ForeignKey(MedicineType, on_delete=models.SET_NULL, blank=True, null=True)
    disease = models.ManyToManyField(Common, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    brand_cn = models.CharField(max_length=200)
    ref_drug_company_name = models.TextField(blank=True, null=True)
    dose = models.TextField(blank=True, null=True)
    packing = models.TextField(blank=True, null=True)
    usage = models.TextField(blank=True, null=True)
    approval_number = models.TextField(blank=True, null=True)
    common_drug = models.ForeignKey(General, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.brand_cn
