import string
from classes.Act import Act
from classes.Songs import Song

class Autoliquidation:
    def __init__(self, array_of_acts: [Act]):
        self.audition_days = None
        self.audition_price = None
        self.contest_days = None
        self.contest_price = None
        self.num_couplets = None
        self.concert_days = None
        self.concert_earnings = None
        self.acts : [Act] = array_of_acts

    def __init__(self, audition_days,audition_price,contest_days,contest_price,num_couplets,concert_days,concert_earnings, array_of_acts: [Act]):
        self.audition_days = audition_days
        self.audition_price = audition_price
        self.contest_days = contest_days
        self.contest_price = contest_price
        self.num_couplets = num_couplets
        self.concert_days = concert_days
        self.concert_earnings = concert_earnings
        self.acts : [Act] = array_of_acts if array_of_acts else []
    
    def add_act(self, act):
        self.acts.append(act)