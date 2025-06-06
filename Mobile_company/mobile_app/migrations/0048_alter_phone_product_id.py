# Generated by Django 5.1.6 on 2025-05-28 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0047_phone_processor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='product_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='phones', serialize=False, to='mobile_app.product'),
        ),
    ]
