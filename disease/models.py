from django.db import models


class Common(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    disease_name = models.CharField(max_length=200)
    department_name = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.disease_name