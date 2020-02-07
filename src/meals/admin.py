from django.contrib import admin

# Register your models here.
from .models import Meals, Category
from django_summernote.admin import SummernoteModelAdmin


class MealsAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = '__all__'
    list_display = ['name', 'preparation_time', 'price']
    search_fields = ['name', 'description']
    list_filter = ('category', 'people')


admin.site.register(Meals, MealsAdmin)
admin.site.register(Category)
