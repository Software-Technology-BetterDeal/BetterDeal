from django.contrib import admin

# Register your models here.

from .models import DummyDatabase

class DummyAdmin(admin.ModelAdmin):
	list_display=('name','price',)

admin.site.register(DummyDatabase,DummyAdmin)