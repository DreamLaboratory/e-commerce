# Generated by Django 3.2.16 on 2023-01-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
    ]
