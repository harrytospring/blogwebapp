from django.contrib import admin
from .models import timeNode
from .models import blog
class timeNodeAdmin(admin.ModelAdmin):
	fields = ['type','time','todoList','doneList']
admin.site.register(timeNode,timeNodeAdmin)
class blogAdmin(admin.ModelAdmin):
	fields = ['classify','created_time','content','title','tips']
admin.site.register(blog,blogAdmin)
# Register your models here.
