# Generated by Django 5.1.5 on 2025-03-04 03:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbvapp', '0002_rename_com_product_company_remove_product_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companies', to='cbvapp.company'),
        ),
    ]
