from django.urls import path
from .views import ArtistList, ArtistDetail, SongList, SongDetail, LyricsList, LyricsDetail

urlpatterns = [
    path('artist', ArtistList.as_view()),
    path('artist/<int:pk>', ArtistDetail.as_view()),
    path('song', SongList.as_view()),
    path('song/<int:pk>', SongDetail.as_view()),
    path('lyrics', LyricsList.as_view()),
    path('lyrics/<int:pk>', LyricsDetail.as_view()),
]