from django.db import models

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    question = models.TextField(verbose_name="问题")
    answer = models.TextField(blank=True, null=True, verbose_name="答案")
    book_name = models.TextField(blank=True, null=True, verbose_name="书名")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "科普书"
        verbose_name_plural = "科普书"


class Video(models.Model):
    id = models.CharField(primary_key=True, max_length=32, verbose_name="ID")
    question = models.TextField(verbose_name="问题")
    answer = models.TextField(blank=True, null=True, verbose_name="答案")
    video_name = models.TextField(blank=True, null=True, verbose_name="视频名称")
    video_program = models.TextField(blank=True, null=True, verbose_name="视频节目")
    video_link = models.TextField(blank=True, null=True, verbose_name="视频链接")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "科普视频"
        verbose_name_plural = "科普视频"
