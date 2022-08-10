from django.contrib import admin
from customer.models import customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fields = ['user','age','weight','height','BMI']
    list_filter = ['user','BMI']
    search_fields = ['user']


admin.site.register(customer,CustomerAdmin)
