from django.db import models

class MedicineType(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    drug_type = models.TextField(verbose_name="药品类型")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.drug_type

    class Meta:
        verbose_name = "药品类型信息"
        verbose_name_plural = "药品类型信息"
