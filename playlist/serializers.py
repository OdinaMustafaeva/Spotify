from rest_framework import serializers
from .models import Music, Playlist, LikeDislike, PlaylistMusic
from category.models import Category
from user.models import User


class MusicAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "full_name")


class MusicCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "title")


class MusicSerializer(serializers.ModelSerializer):
    category = MusicCategorySerializer()
    author = MusicAuthorSerializer()

    class Meta:
        model = Music
        fields = (
            "id", "author", "title", "slug", "image", "category", "collab", "likes", "dislikes"
        )


class MusicDetailSerializer(serializers.ModelSerializer):
    category = MusicCategorySerializer()
    author = MusicAuthorSerializer()

    class Meta:
        model = Music
        fields = (
            "id", "author", "title", "slug", "image", "category", "collab", "lyrics", "likes", "dislikes, "
        )


class PlaylistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)


    class Meta:
        model = Playlist
        fields = ("id", "title", "image", "song")


class MusicCreateSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(required=False)
    category = MusicCategorySerializer()
    author = MusicAuthorSerializer()

    class Meta:
        model = Music
        fields = ["id", "author", "title", "slug", "image", "category", "collab", "lyrics", "likes", "dislikes"]


class MusicLikeDislikeSerializer(serializers.Serializer):
    type = serializers.ChoiceField(choices=LikeDislike.LikeType.choices)
