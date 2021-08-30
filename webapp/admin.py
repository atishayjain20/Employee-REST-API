from django.contrib import admin
from .models import empoylee
# Register your models here.
@admin.register(empoylee)
class employeAdmin(admin.ModelAdmin):
    list_display=['firstname','lastname','emp_id']
