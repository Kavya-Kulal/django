# Generated by Django 5.1.6 on 2025-03-21 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.AutoField(primary_key=True, serialize=False)),
                ('collection_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_id', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmarks', to='app1.collection')),
            ],
        ),
    ]
