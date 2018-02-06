from django.contrib import admin
from .models import Visit

# Register your models here.
class VisitAdmin(admin.ModelAdmin):
	list_display = ['number', 'date', 'visited', 'ip_address', 'asn', 'country']
	list_filter = ['visited']
	class Meta:
		model = Visit
admin.site.register(Visit, VisitAdmin)