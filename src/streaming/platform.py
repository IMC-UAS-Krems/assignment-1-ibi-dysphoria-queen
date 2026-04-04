"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
class Streamingplatform:
    catalogue ={}
    users ={}
    artists ={}
    albums ={}
    playlists ={}
    sessions ={}
    def __init__(self,name: str,):
        self.name = name
    def add_track(self,track):
        self.catalogue.update({track.name:track})
    def add_user(self,user):
        self.users.update({user.name:user})
    def add_artist(self,artist):
        self.artists.update({artist.name:artist})
    def add_album(self,album):
        self.albums.update({album.name:album})
    def add_playlist(self,playlist):
        self.playlists.update({playlist.name:playlist})
    def record_session(self,session):
        self.sessions.update({session.name:session})
    def get_track(self,track_id):
        return self.catalogue.get(track_id)
    def get_user(self,user_id):
        return self.users.get(user_id)
    def get_artist(self,artist_id):
        return self.artists.get(artist_id)
    def get_album(self,album_id):
        return self.albums.get(album_id)
    def get_playlist(self,playlist_id):
        return self.playlists.get(playlist_id)
    def allusers(self):
        return self.users
    def alltracks(self):
        return self.catalogue
