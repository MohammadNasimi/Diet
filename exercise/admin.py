from django.contrib import admin

# Register your models here.
from django.contrib import admin
from exercise.models import exercise
# Register your models here.
class exerciseAdmin(admin.ModelAdmin):
    fields = ['name_exercise','calories','time']
    list_filter = ['name_exercise']
    search_fields = ['name_exercise']


admin.site.register(exercise,exerciseAdmin)