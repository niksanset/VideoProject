# Generated by Django 5.0.4 on 2024-04-18 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_title_director_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='director',
        ),
        migrations.AddField(
            model_name='comment',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.media'),
        ),
    ]
