# Generated by Django 5.0 on 2023-12-28 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0004_status_apartment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choise_room', to='apartment.status'),
        ),
    ]
