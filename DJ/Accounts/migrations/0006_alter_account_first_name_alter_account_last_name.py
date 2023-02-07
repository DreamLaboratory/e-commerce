# Generated by Django 4.1.5 on 2023-02-02 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0005_profile_first_name_profile_image_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='last_name'),
        ),
    ]