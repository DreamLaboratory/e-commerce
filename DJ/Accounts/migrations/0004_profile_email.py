# Generated by Django 4.1.5 on 2023-01-26 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0003_remove_account_auth_token_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]