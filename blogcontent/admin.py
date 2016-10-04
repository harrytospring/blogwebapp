from django.contrib import admin
from .models import timeNode
class timeNodeAdmin(admin.ModelAdmin):
	fields = ['type','time','todoList','doneList']
admin.site.register(timeNode,timeNodeAdmin)
# Register your models here.
