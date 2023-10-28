from Songs import Song
import string

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