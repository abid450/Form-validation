from django.contrib import admin
from .models import todo
# Register your models here.
admin.site.register(todo)
class todoModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Password','text']