from django.contrib import admin

# Register your models here.
from .models import RecipeIngredient, Recipe

admin.site.register(RecipeIngredient)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['user', 'name']
    readonly_fields = ['user', 'timestamp', 'updated']


admin.site.register(Recipe, RecipeAdmin)