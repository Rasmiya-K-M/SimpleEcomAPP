from django.contrib import admin
from . models import Category,Product
# Register your models here.
class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name','price','stock','avail','created','updated']
    list_editable = ['price','stock','avail']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,productadmin)