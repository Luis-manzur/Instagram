from django.contrib import admin

from posts.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'photo', 'created')
    search_fields = ('user', 'title')
    list_display_link = ('pk', )
    list_editable = ('photo', 'title')
    list_filter = ('created', 'modified')