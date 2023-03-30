from django.contrib import admin

# Register your models here.
from .models import RecipeIngredient, Recipe

admin.site.register(RecipeIngredient)

class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    #fields = ['name', 'quanity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInLine]
    list_display = ['user', 'name']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)