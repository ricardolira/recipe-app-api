# Generated by Django 2.1.11 on 2019-08-13 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_ingredients'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredients',
            new_name='Ingredient',
        ),
    ]