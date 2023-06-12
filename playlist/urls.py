from django.urls import path

from .views import MusicDetailView, MusicLikeDislikeView, MusicListCreateView

urlpatterns = [
    path("", MusicListCreateView.as_view(), name="music_list_create"),
    path("<slug:slug>/like_dislike/", MusicLikeDislikeView.as_view(), name="music_like_dislike"),
    path("<slug:slug>/", MusicDetailView.as_view(), name="music_detail"),
]
