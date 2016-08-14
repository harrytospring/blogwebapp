from django.contrib import admin
from .models import blog_content
class blog_contentAdmin(admin.ModelAdmin):
	fields = ['blog_head','blog_text']
admin.site.register(blog_content,blog_contentAdmin)
# Register your models here.
