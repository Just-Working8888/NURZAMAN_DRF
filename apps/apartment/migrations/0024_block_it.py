# Generated by Django 5.0 on 2024-01-02 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0023_block_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='it',
            field=models.IntegerField(blank=True, null=True, verbose_name='Нумерация'),
        ),
    ]
