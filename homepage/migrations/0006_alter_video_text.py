# Generated by Django 4.2.14 on 2024-07-18 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_video_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
    ]
