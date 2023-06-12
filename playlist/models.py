import random

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Music(TimestampModel):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_author")
    title = models.CharField(_("Title"), max_length=200)
    slug = models.SlugField(unique=True)
    music = models.FileField(upload_to="song")
    image = models.ImageField(_("image"), null=True, upload_to="music")
    category = models.ForeignKey("category.Category", on_delete=models.CASCADE, related_name="categories")
    collab = models.ManyToManyField(
        "user.User", related_name='collab', blank=True)
    lyrics = models.TextField(null=True, max_length=400)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        slug = self.slug
        while self.__class__.objects.filter(slug=slug).exists():
            slug = f"{self.slug}-{random.randint(1, 100000)}"
        self.slug = slug
        return super().save(*args, **kwargs)

    @property
    def likes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.LIKE).count()

    @property
    def dislikes(self):
        return self.like_dislikes.filter(type=LikeDislike.LikeType.DISLIKE).count()

    def __str__(self):
        return f"{self.title}"


class Playlist(TimestampModel):
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_playlist")
    title = models.CharField(_("Title"), max_length=200)
    image = models.ImageField(_("image"), null=True, upload_to="playlist")

    def __str__(self):
        return f"{self.title}"

    @property
    def song(self):
        return self.playlist_music.all().count()


class PlaylistMusic(TimestampModel):
    playlist = models.ForeignKey("playlist.Playlist", on_delete=models.CASCADE, related_name="playlist_music")
    song = models.ForeignKey("playlist.Music", on_delete=models.CASCADE, related_name="song")

    def __str__(self):
        return f"{self.song.title}"


class LikeDislike(TimestampModel):
    class LikeType(models.IntegerChoices):
        DISLIKE = -1
        LIKE = 1

    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="like_dislikes")
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="user_like_dislike")
    type = models.SmallIntegerField(choices=LikeType.choices)

    class Meta:
        unique_together = ["music", "user"]

    def __str__(self):
        return f"{self.user}"
