from django.contrib import admin

from .models import projecto

# Register your models here.

class ProjectoAdmin(admin.ModelAdmin):
	readonly_fields  = ('creacion','actualizacion')

admin.site.register(projecto,ProjectoAdmin)