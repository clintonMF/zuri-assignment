from rest_framework import generics

from .models import Song, Lyrics, Artist
from .serializers import ArtistSerializer, LyricsSerializer, SongSerializer

class ArtistList(generics.ListCreateAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
    
class SongList(generics.ListCreateAPIView):
    serializer_class = SongSerializer
    
    def get_queryset(self):
        queryset = Song.objects.all()
        artist = self.request.query_params.get('artist')
        if artist is not None:
            queryset = queryset.filter(artiste_id = artist)
        return queryset
    
class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SongSerializer
    queryset = Song.objects.all()
    
class LyricsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LyricsSerializer
    queryset = Lyrics.objects.all()
    
class LyricsList(generics.ListCreateAPIView):
    serializer_class = LyricsSerializer
    
    def get_queryset(self):
        queryset = Lyrics.objects.all()
        song = self.request.query_params.get('song')
        if song is not None:
            queryset = queryset.filter(song_id = song)
        return queryset