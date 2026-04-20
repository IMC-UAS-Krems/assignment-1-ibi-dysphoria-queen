"""
albums.py
---------
Implement the Album class for collections of AlbumTrack objects.

Classes to implement:
  - Album
"""
import datetime
from streaming import tracks


class Album:
    tracks=[]
    def __init__(self,album_id, title, artist, album_type):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.album_type = album_type
    def addTrack(self,track):
        self.tracks.append(track)
    def trackid(self):
        track_id =[]
        for i in range(len(self.tracks)):
            track_id.append(tracks[i].track_id)
        return track_id
    def duration_seconds(self):
        total = 0
        for track in self.tracks:
            total += (track.duration_minutes) * 60
        return total