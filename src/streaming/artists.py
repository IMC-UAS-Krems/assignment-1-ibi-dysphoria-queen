"""
artists.py
----------
Implement the Artist class representing musicians and content creators.

Classes to implement:
  - Artist
"""

class Artist:
    tracks=[]
    def __init__(self,artist_id,name,genre):
        self.artist_id = artist_id
        self.name = name
        self.genre = genre
    def add_track(self,track):
        self.tracks.append(track)
    def track_count(self):
        return len(self.tracks)