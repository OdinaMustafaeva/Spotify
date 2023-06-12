# Generated by Django 4.2.2 on 2023-06-12 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('playlist', '0001_initial'),
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_playlist', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='music',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='music',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='category.category'),
        ),
        migrations.AddField(
            model_name='music',
            name='collab',
            field=models.ManyToManyField(blank=True, related_name='collab', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_dislikes', to='playlist.music'),
        ),
        migrations.AddField(
            model_name='likedislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_like_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='likedislike',
            unique_together={('music', 'user')},
        ),
    ]
