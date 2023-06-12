from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Music, LikeDislike, Playlist
from .serializers import MusicLikeDislikeSerializer, MusicSerializer, MusicCreateSerializer, \
    PlaylistSerializer, MusicDetailSerializer
from paginations import CustomPageNumberPagination


class MusicListCreateView(generics.ListCreateAPIView):
    queryset = Music.objects.order_by("-id")
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    filterset_fields = ("category", "author")
    ordering_fields = ("id", "slug", "author", "title")
    search_fields = ("title", "category__title", "author")
    pagination_class = CustomPageNumberPagination

    def get_serializer_class(self):
        if self.request.method == "POST":
            return MusicCreateSerializer
        return MusicSerializer


class MusicDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return MusicCreateSerializer
        return MusicDetailSerializer


class MusicLikeDislikeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = MusicLikeDislikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        type_ = serializer.validated_data.get("type")
        user = request.user
        music = Music.objects.filter(slug=self.kwargs.get("slug")).first()
        if not music:
            raise Http404
        like_dislike_blog = LikeDislike.objects.filter(music=music, user=user).first()
        if like_dislike_blog and like_dislike_blog.type == type_:
            like_dislike_blog.delete()
        else:
            LikeDislike.objects.update_or_create(music=music, user=user, defaults={"type": type_})
        data = {"type": type_, "detail": "Liked or disliked."}
        return Response(data)


class PlaylistView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PlaylistSerializer
        return PlaylistSerializer


class PlaylistDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Playlist.objects.all()
    lookup_field = "id"

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            return PlaylistSerializer
        return PlaylistSerializer
