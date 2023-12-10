from classes.Songs import Song
import string

class Act:
    def __init__(self):
        self.number : string= ""
        self.title :string = ""
        self.local_name :string = ""
        self.city :string = ""
        self.province:string = ""
        self.init_date:string = ""
        self.end_date:string = ""
        self.songs =  []

    def __init__(self, number=None, title=None, local_name=None, city=None, province=None, init_date=None, end_date=None, songs=None):
        self.number = number
        self.title = title
        self.local_name = local_name
        self.city = city
        self.province = province
        self.init_date = init_date
        self.end_date = end_date
        self.songs = songs if songs else []

    def add_song(self, song):
        self.songs.append(song)
