# Generated by Django 4.2.2 on 2023-06-12 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlist', '0003_playlist_title_en_playlist_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]