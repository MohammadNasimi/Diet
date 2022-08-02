from django.contrib import admin

from food.models import food

# Register your models here.
class foodAdmin(admin.ModelAdmin):
    fields = ['name','calories','mesure']
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(food,foodAdmin)
