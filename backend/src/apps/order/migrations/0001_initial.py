# Generated by Django 3.2.16 on 2023-02-25 10:30

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0004_auto_20230218_1555'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_number', models.CharField(max_length=255, unique=True)),
                ('f_name', models.CharField(max_length=255)),
                ('l_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=50)),
                ('regions', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('order_note', ckeditor.fields.RichTextField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ip', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('NEW', 'Новый'), ('IN_PROGRESS', 'В обработке'), ('DONE', 'Выполнен'), ('CANCELED', 'Отменен')], default='NEW', max_length=255)),
                ('cart_items', models.ManyToManyField(related_name='orders', to='cart.CartItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
