# Generated by Django 5.1.6 on 2025-03-18 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_collection_delete_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='created_at',
        ),
    ]
