# Generated by Django 4.1.6 on 2023-03-30 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="RecipeIngredients",
            new_name="RecipeIngredient",
        ),
    ]
