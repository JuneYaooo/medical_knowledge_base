from django.db import models

class Common(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    disease_name = models.CharField(max_length=200, verbose_name="疾病名称")
    department_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="科室名称")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.disease_name

    class Meta:
        verbose_name = "常见疾病信息"
        verbose_name_plural = "常见疾病信息"
