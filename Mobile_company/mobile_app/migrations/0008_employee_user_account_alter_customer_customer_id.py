# Generated by Django 5.1.6 on 2025-04-19 16:52

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0007_remove_camera_id_remove_camera_product_id_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='user_account',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
