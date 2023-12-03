import string
from classes.Act import Act
from classes.Songs import Song

class Organization:
    def __init__(self, array_of_acts: [Act]):
        self.acts : [Act] = array_of_acts
        self.number : string = ""
        self.name : string = ""
        self.orchestra : string = ""
        self.place : string = ""
        self.order_place : string = ""
        self.city : string = ""
        self.province : string = ""
        self.representator_name : string = ""
        self.direction : string = ""
        self.postal_code : string = ""
        self.city : string = ""
        self.province : string = ""
        self.mail : string = ""
        self.mobile : string = ""
        self.sgae_code : string = ""
        self.initial_date : string = ""
        self.final_date : string = ""
        self.representator_dni : string = ""

    def __init__(self,acts: [Act],number=None,name=None,orchestra=None,place=None,order_place=None,city=None,province=None,representator_name=None,direction=None,postal_code=None,mail=None,mobile=None,sgae_code=None,initial_date=None,final_date=None,representator_dni=None):
        self.acts = acts 
        self.number = number 
        self.name = name 
        self.orchestra = orchestra 
        self.place = place 
        self.order_place = order_place 
        self.city = city 
        self.province = province 
        self.representator_name = representator_name 
        self.direction = direction 
        self.postal_code = postal_code 
        self.city = city 
        self.province = province 
        self.mail = mail 
        self.mobile = mobile 
        self.sgae_code = sgae_code 
        self.initial_date = initial_date 
        self.final_date = final_date 
        self.representator_dni = representator_dni 
    
    def add_act(self, act):
        self.acts.append(act)

