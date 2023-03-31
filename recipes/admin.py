from django.contrib import admin
from django.contrib.auth import get_user_model

# Register your models here.
from .models import RecipeIngredient, Recipe

User = get_user_model()

admin.site.register(RecipeIngredient)

class UserInline(admin.ModelAdmin):
    model = User

class RecipeIngredientInLine(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    #fields = ['name', 'quanity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [UserInline, RecipeIngredientInLine]
    list_display = ['user', 'name']
    readonly_fields = ['timestamp', 'updated']
    raw_id_fields = ['user']


admin.site.register(Recipe, RecipeAdmin)