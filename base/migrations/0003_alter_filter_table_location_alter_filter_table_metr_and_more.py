# Generated by Django 5.0.2 on 2024-02-15 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_filter_table_parking_alter_filter_table_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filter_table',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter_table',
            name='metr',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter_table',
            name='parking',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter_table',
            name='price',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='filter_table',
            name='rooms',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
