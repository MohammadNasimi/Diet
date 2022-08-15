from django.contrib import admin
from Diet.models import Diet,Diet_admin
# Register your models here.
class DietAdmin(admin.ModelAdmin):
    fields = ['user','food_Diet','exercise_Diet','kind_diet']
    list_filter = ['user']
    search_fields = ['user']
admin.site.register(Diet,DietAdmin)

class Diet_adminAdmin(admin.ModelAdmin):
    fields = ['user_admin','food_Diet_admin','exercise_Diet_admin']
    list_filter = ['user_admin']
    search_fields = ['user_admin']
admin.site.register(Diet_admin,Diet_adminAdmin)
