from django.contrib import admin

from food.models import food ,food_diet_user

# Register your models here.
class foodAdmin(admin.ModelAdmin):
    fields = ['name','calories','mesure']
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(food,foodAdmin)

class food_diet_userAdmin(admin.ModelAdmin):
    fields = ['customer_food','food_field','mesure_food_customer']
    list_filter = ['customer_food']
    search_fields = ['customer_food']
admin.site.register(food_diet_user,food_diet_userAdmin)
