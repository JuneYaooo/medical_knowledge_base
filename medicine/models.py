from django.db import models
from dim.models import MedicineType
from disease.models import Common

class General(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    name = models.CharField(max_length=200, verbose_name="通用名称")
    name_en = models.CharField(max_length=200, blank=True, null=True, verbose_name="英文名称")
    department_category = models.CharField(max_length=200, blank=True, null=True, verbose_name="科室类别")
    medical_insurance_status = models.CharField(max_length=200, blank=True, null=True, verbose_name="医保状态")
    children_taboo = models.TextField(blank=True, null=True, verbose_name="儿童禁忌")
    pregnant_women_taboo = models.TextField(blank=True, null=True, verbose_name="孕妇禁忌")
    elderly_taboo = models.TextField(blank=True, null=True, verbose_name="老年人禁忌")
    indications = models.TextField(blank=True, null=True, verbose_name="适应症")
    contraindication = models.TextField(blank=True, null=True, verbose_name="禁忌症")
    adr = models.TextField(blank=True, null=True, verbose_name="不良反应")
    note = models.TextField(blank=True, null=True, verbose_name="注意事项")
    interaction = models.TextField(blank=True, null=True, verbose_name="药物相互作用")
    storage = models.TextField(blank=True, null=True, verbose_name="存储方法")
    ingredient = models.TextField(blank=True, null=True, verbose_name="成分")
    dosage_form = models.TextField(blank=True, null=True, verbose_name="剂型")
    medical_type = models.ForeignKey(MedicineType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="药品类型")
    disease = models.ManyToManyField(Common, blank=True, verbose_name="相关疾病")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "通用药品信息"
        verbose_name_plural = "通用药品信息"


class Brand(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    brand_cn = models.CharField(max_length=200, verbose_name="商品名称")
    ref_drug_company_name = models.TextField(blank=True, null=True, verbose_name="药企名称")
    dose = models.TextField(blank=True, null=True, verbose_name="剂量")
    packing = models.TextField(blank=True, null=True, verbose_name="包装")
    usage = models.TextField(blank=True, null=True, verbose_name="用法")
    approval_number = models.TextField(blank=True, null=True, verbose_name="批准文号")
    common_drug = models.ForeignKey(General, on_delete=models.CASCADE, verbose_name="通用药品")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.brand_cn

    class Meta:
        verbose_name = "商品名称信息"
        verbose_name_plural = "商品名称信息"
