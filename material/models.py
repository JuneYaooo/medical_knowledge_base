from django.db import models

class Book(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    book_name = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Video(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    video_name = models.TextField(blank=True, null=True)
    video_program = models.TextField(blank=True, null=True)
    video_link = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question
