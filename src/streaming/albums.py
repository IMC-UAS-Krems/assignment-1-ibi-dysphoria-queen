"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
import datetime
from streaming import sessions, users, playlists, tracks, artists


class Album:
    tracks=[]
    def __init__(self,album_id, title, artist, release_year):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.release_year = release_year
    def add_track(self,track):
        self.tracks.append(track)
        track.album = self
    def track_ids(self):
        track_id =[]
        for i in range(len(self.tracks)):
            track_id.append(tracks[i].track_id)
        return track_id
    def duration_seconds(self):
        total = 0
        for track in self.tracks:
            total += track.duration_seconds
        return total