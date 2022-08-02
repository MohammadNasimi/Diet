from django.contrib import admin
from Diet.models import Diet
# Register your models here.
class DietAdmin(admin.ModelAdmin):
    fields = ['user','food_Diet','exercise_Diet']
    list_filter = ['user']
    search_fields = ['user']
admin.site.register(Diet,DietAdmin)