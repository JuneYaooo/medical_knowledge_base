from django.contrib import admin
from .models import Video, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'book_name')
    search_fields = ('question', 'book_name')

class VideoAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'video_name')
    search_fields = ('question', 'video_name')

admin.site.register(Book, BookAdmin)
admin.site.register(Video, VideoAdmin)
