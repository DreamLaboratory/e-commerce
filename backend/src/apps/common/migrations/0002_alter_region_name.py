# Generated by Django 3.2.16 on 2023-03-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
