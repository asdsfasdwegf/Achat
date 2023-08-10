from django.contrib import admin
from .models import Post, Comment
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'update')
    search_fields = ('slug',)
    list_filter = ('update',)
    prepopulated_fields = {'slug':('body',)}
    raw_id_fields = ('user', )
admin.site.register(Post)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','post','created')
    raw_id_fields = ('user','post','reply')
admin.site.register(Comment)
