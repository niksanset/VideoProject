# Generated by Django 5.0.4 on 2024-04-18 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_comment_director_comment_media'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
