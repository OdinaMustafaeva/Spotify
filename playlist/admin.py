from django.contrib import admin
from .models import Music, LikeDislike, Playlist, PlaylistMusic
from modeltranslation.admin import TranslationAdmin, TabbedTranslationAdmin


# Register your models here.


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "category"]


@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ["user", "music", "type"]


@admin.register(Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["author", "title"]


@admin.register(PlaylistMusic)
class PlaylistAdmin(admin.ModelAdmin):
    list_display = ["playlist", "song"]
