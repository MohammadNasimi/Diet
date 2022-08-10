from django.contrib import admin

# Register your models here.
from django.contrib import admin
from exercise.models import exercise,exercise_diet_user
# Register your models here.
class exerciseAdmin(admin.ModelAdmin):
    fields = ['name_exercise','calories','time']
    list_filter = ['name_exercise']
    search_fields = ['name_exercise']


admin.site.register(exercise,exerciseAdmin)

class exercise_diet_userAdmin(admin.ModelAdmin):
    fields = ['customer_exercise','exersise_field','time_exercise_customer']
    list_filter = ['customer_exercise']
    search_fields = ['customer_exercise']


admin.site.register(exercise_diet_user,exercise_diet_userAdmin)