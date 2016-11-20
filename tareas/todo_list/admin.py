from django.contrib import admin
from todo_list.models import tarea, proyecto

class ItemAdmin(admin.ModelAdmin):
	list_display = ["name", "priority", "difficulty", "creation_date"]
	searcg_fields = ["name"]

admin.site.register(tarea, ItemAdmin)
admin.site.register(proyecto)
