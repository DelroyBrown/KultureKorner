# Generated by Django 5.0.6 on 2024-07-09 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KultureKorner_postArt', '0003_rename_past_date_postart_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postart',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
        migrations.AlterField(
            model_name='postart',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
        migrations.AlterField(
            model_name='postart',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
        migrations.AlterField(
            model_name='postart',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
        migrations.AlterField(
            model_name='postart',
            name='image_5',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
        migrations.AlterField(
            model_name='postart',
            name='image_6',
            field=models.ImageField(blank=True, null=True, upload_to='artImage'),
        ),
    ]
