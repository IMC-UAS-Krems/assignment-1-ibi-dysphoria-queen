"""
platform.py
-----------
Implement the central StreamingPlatform class that orchestrates all domain entities
and provides query methods for analytics.

Classes to implement:
  - StreamingPlatform
"""
import datetime
from itertools import count

from streaming import sessions, users, playlists
from streaming.users import PremiumUser

class StreamingPlatform :
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
    def all_users(self):
        return self.users
    def all_tracks(self):
        return self.catalogue
    def total_listening_time_minutes(self,start, end):
        counter =0
        for session in self.sessions:
            if session.start_time <= start and session.end_time >= end:
                counter += session.total_listening_time_minutes
        return counter
    def avg_unique_tracks_per_premium_user(self,days: int = 30):
        counter =[]
        no_of_premium_users = 0
        last30days= datetime.datetime.now()
        last30days.days = last30days.day - days
        for session in self.sessions:
            if type(session.user).__name__ == 'PremiumUser':
                if session.start_time <= last30days and session.end_time > last30days :
                    counter.append(session.track)
                    no_of_premium_users += 1
        counter=list(set(counter))
        return len(counter)/no_of_premium_users
    def track_with_most_distinct_listeners(self):
        listofusers =[]
        tracks ={}
        for session in self.sessions:
            if session.user in listofusers:
                pass
            else:
                listofusers.append(session.user)
                tracks[session.track]+=1
        sorted_tracks = dict(sorted(tracks.items(), key=lambda item: item[1], reverse=True))
        return next(iter(sorted_tracks)).keys

    def top_artists_by_listening_time(self,n: int = 5):
        artists ={}
        for session in sessions:
            if type(session.Track).__name__ == 'Song':
                if session.Track.artist in artists:
                    artists[session.Track.artist]+=1
                else:
                    artists.update({session.Track.artist:1})
        sorted_artists = dict(sorted(artists.items(), key=lambda item: item[1], reverse=True))
        sorted_artists_list = list(sorted_artists.items())
        return sorted_artists_list[:n]
    def avg_session_duration_by_user_type(self):
        users ={}
        listening_times ={}
        for session in sessions:
            if type(session.user).__name__ == 'FreeUser':
                users["FreeUser"]+=1
                listening_times["FreeUser"]+=session.duration
            elif  type(session.user).__name__ == 'PremiumUser':
                users["PremiumUser"]+=1
                listening_times["PremiumUser"]+=session.duration
            elif type(session.user).__name__ == 'FamilyAccountUser':
                users["FamilyAccountUser"]+=1
                listening_times["FamilyAccountUser"]+=session.duration
            elif type(session.user).__name__ == 'FamilyMember':
                users["FamilyMember"]+=1
                listening_times["FamilyMember"]+=session.duration
        listening_times["FreeUser"]=listening_times["FreeUser"]/users["FreeUser"]
        listening_times["PremiumUser"]=listening_times["PremiumUser"]/users["PremiumUser"]
        listening_times["FamilyAccountUser"]=listening_times["FamilyAccountUser"]/users["FamilyMember"]
        listening_times["FamilyMember"]=listening_times["FamilyMember"]/users["FamilyMember"]
        return  list(listening_times.items())

    def total_listening_time_underage_sub_users_minutes(self,age_threshold: int = 18):
        counter =0
        for session in self.sessions:
            if session.user.age < age_threshold:
                counter += session.total_listening_time_minutes
        return counter

    def user_top_genre(self,userid):
        genres ={}
        counter =0
        for session in self.sessions:
            if session.user.user_id == userid:
                counter += 1
                genres[session.track.genre]+=1
        sorted_genres = dict(sorted(genres.items(), key=lambda item: item[1], reverse=True))
        largestgenre = next(iter(sorted_genres))
        largestgenre = largestgenre/counter
        return largestgenre.items()

    def collaborative_playlists_with_many_artists(self,threshold: int = 3):
        counter =[]
        for playlist in self.playlists:
            if type(playlist).__name__ == 'CollaborativePlaylist':
                if len(playlist.contributors)>=3:
                    counter.append(playlist)
        return counter

   def avg_tracks_per_playlist_type(self):
        playlisttypes ={"Playlist":float(0),
                    "CollaborativePlaylist":float(0)}
        playliststracks = {"Playlist": float(0),
                     "CollaborativePlaylist": float(0)}
        for playlist in self.playlists:
            if type(playlist).__name__ == 'CollaborativePlaylist':
                playlisttypes["CollaborativePlaylist"]+=1
                playliststracks["CollaborativePlaylist"]+=len(playlist.tracks)
            else:
                playlisttypes["Playlist"]+=1
                playliststracks["Playlist"]+=len(playlist.tracks)
        playliststracks["Playlist"]=playliststracks["Playlist"]/playlisttypes["Playlist"]
        playliststracks["CollaborativePlaylist"]=playliststracks["CollaborativePlaylist"]/playlisttypes["CollaborativePlaylist"]
        return playliststracks


