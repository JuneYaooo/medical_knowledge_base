from django.db import models


class MedicineType(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    drug_type = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.drug_type