# Generated by Django 2.2.5 on 2022-09-05 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220905_1507'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recipes',
            new_name='Recipe',
        ),
    ]
