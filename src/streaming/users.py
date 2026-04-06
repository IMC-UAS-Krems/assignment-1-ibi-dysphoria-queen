"""
users.py
--------
Implement the class hierarchy for platform users.

Classes to implement:
  - User (base class)
    - FreeUser
    - PremiumUser
    - FamilyAccountUser
    - FamilyMember
"""
from samba.dcerpc.smb_acl import user


class User:
    sessions=[]
    def __init__(self, name, user_id,age):
        self.name = name
        self.user_id = user_id
        self.age = age
    def add_session(self,session):
        self.sessions.append(session)
    def total_listening_seconds(self):
        count = 0
        for session in self.sessions:
            count =+ session.duration_listened_seconds
        return count
    def total_listening_minutes(self):
        count = 0
        for session in self.sessions:
            count =+ session.duration_listened_minutes()
        return count
    def unique_tracks_listened(self):
        count =[]
        for session in self.sessions:
            if session.name not in count:
                count.append(session.session_id)
class FreeUser(User):
    MAX_SKIPS_PER_HOUR = 6
    def __init__(self, name, user_id,age):
        super().__init__(name,user_id,age)
class PremiumUser(User):
    def __init__(self, name, user_id,age,subscription_start):
        super().__init__(name,user_id,age)
        self.subscription_start = subscription_start
class FamilyAccount(user):
    sub_users=[]
    def __init__(self,name,user_id,age):
        super().__init__(name,user_id,age)
    def add_sub_user(self,sub_user):
        self.sub_users.append(sub_user)
    def all_members(self):
        return self.sub_users

class FamilyMember(user):
    def __init__(self,name,user_id,age):
        super().__init__(name,user_id,age)