"""
playlists.py
------------
Implement playlist classes for organizing tracks.

Classes to implement:
  - Playlist
    - CollaborativePlaylist
"""
import datetime
from streaming import sessions, users, tracks, artists, albums
class Playlist:
    tracks = []
    def __init__(self,playlist_id,name,owner):
        self.playlist_id = playlist_id
        self.name = name
        self.owner = owner
    def add_track(self,track):
        self.tracks.append(track)
    def remove_track(self,track_id):
        for track in self.tracks:
            if track.track_id == track_id:
                self.tracks.remove(track)
    def total_duration_seconds(self):
        total = 0
        for track in self.tracks:
            total += track.duration_seconds
        return total
class CollaborativePlaylist(Playlist):
    contributors = []
    def __init__(self,playlist_id,name,owner):
        super().__init__(playlist_id,name,owner)
    def add_contributor(self,contributor):
        self.contributors.append(contributor)
    def remove_contributor(self,contributor):
        self.contributors.remove(contributor)