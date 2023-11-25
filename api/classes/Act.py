from classes.Songs import Song
import string

"""
class Act:
    def __init__(self):
        self.songs: [Song] = []
        self.title: string = None
        self.event_number: int = None
        self.local_name: string = None
        self.order_number: int = None
        self.invoice_number: int = None
        self.city: string = None
        self.province: string = None
        self.liq_included: bool = None
        self.sheet_number: int = None
        self.title_number: int = None
        self.parts: int = None
        self.area_tit: int = None
        self.day: int = None
        self.month: int = None
        self.year: int = None
        self.init_date: string = None
        self.end_date: string = None

    
    def __init__(self, Song1):
        self.title: string = None
        self.event_number: int = None
        self.local_name: string = None
        self.order_number: int = None
        self.invoice_number: int = None
        self.city: string = None
        self.province: string = None
        self.liq_included: bool = None
        self.sheet_number: int = None
        self.title_number: int = None
        self.parts: int = None
        self.area_tit: int = None
        self.day: int = None
        self.month: int = None
        self.year: int = None
        self.init_date: string = None
        self.end_date: string = None
        self.songs: [Song] = [Song1]
"""
class Act:
    def __init__(self, title=None, event_number=None, local_name=None, order_number=None, 
                 invoice_number=None, city=None, province=None, liq_included=None, 
                 sheet_number=None, title_number=None, parts=None, area_tit=None, 
                 day=None, month=None, year=None, init_date=None, end_date=None, songs=None):
        self.title = title
        self.event_number = event_number
        self.local_name = local_name
        self.order_number = order_number
        self.invoice_number = invoice_number
        self.city = city
        self.province = province
        self.liq_included = liq_included
        self.sheet_number = sheet_number
        self.title_number = title_number
        self.parts = parts
        self.area_tit = area_tit
        self.day = day
        self.month = month
        self.year = year
        self.init_date = init_date
        self.end_date = end_date
        self.songs = songs if songs else []

    def add_song(self, song):
        self.songs.append(song)
