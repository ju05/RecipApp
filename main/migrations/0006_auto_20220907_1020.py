# Generated by Django 2.2.5 on 2022-09-07 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20220906_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='carbs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='fat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
