from django.contrib import admin
from .models import todo
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('text','is_completed','created_at','updated_at');search_fields = ('text',)
admin.site.register(todo, TaskAdmin)