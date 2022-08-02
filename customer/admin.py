from django.contrib import admin
from customer.models import customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fields = ['user']
    list_filter = ['user']
    search_fields = ['user']


admin.site.register(customer,CustomerAdmin)
