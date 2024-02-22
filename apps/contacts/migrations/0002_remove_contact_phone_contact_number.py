# Generated by Django 5.0 on 2023-12-17 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='number',
            field=models.CharField(default=1, max_length=255, verbose_name='Телефонный номер'),
            preserve_default=False,
        ),
    ]