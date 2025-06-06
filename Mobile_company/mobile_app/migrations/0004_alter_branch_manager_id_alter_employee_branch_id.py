# Generated by Django 5.1.6 on 2025-04-05 03:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_app', '0003_alter_employee_branch_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='manager_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mobile_app.employee'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='branch_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='mobile_app.branch'),
            preserve_default=False,
        ),
    ]
