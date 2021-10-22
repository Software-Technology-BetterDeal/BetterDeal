from django.contrib import admin

# Register your models here.

from .models import Product

class DummyAdmin(admin.ModelAdmin):
	list_display=('product_name','price','supermarket',)

admin.site.register(Product,DummyAdmin)