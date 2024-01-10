import os
import csv
import pandas as pd
from classes.Songs import Song
from classes.objectInstances import Objects
from classes.Organization import Organization
from classes.Act import Act
from classes.Autoliquidation import Autoliquidation
class CSVWriter:
    def __init__(self):
        self.data_list = []

    # One for each team, registering a file
    def collect_SGAE_data(self, Organization: Organization, Act: Act):
        program = Objects().get_Program()
        program["Nº programa"] = Organization.number
        program["título del espectáculo"] = Act.title
        # program["Valoración del Programa"] = str("\ ")
        program["Orquesta o cobla"] = Organization.orchestra
        # program["Evento n"] = str("\ ")
        program["Local"] = Act.local_name
        # program["Cód Local"] = str("\ ")
        # program["Pedido n"] = str("\ ")
        program["Domicilio"] = Organization.order_place
        # program["Factura n"] = str("\ ")
        program["Población"] = Act.city
        program["Provincia"] = Act.province
        # program["Incluido en liquidación"] = str("\ ")
        # program["N de hojas"] = str("\ ")
        program["Nombre del declarante"] = Organization.representator_name
        # program["N de títulos"] = str("\ ")
        # program["Partes"] = str("\ ")
        program["Dirección"] = Organization.direction
        program["CP"] = Organization.postal_code
        program["Población_2"] = Act.city
        program["Provincia_2"] = Act.province
        program["Correo electrónico"] = Organization.mail
        # program["D"] = str("\ ")
        program["Teléfono"] = Organization.mobile
        program["Código socio SGAE"] = Organization.sgae_code
        # program["Titular de Zona N"] = str("\ ")
        # program["Fecha"] = str("\ ")
        # program["de"] = str("\ ")
        # program["año"] = str("\ ")
        program["desde fecha"] = Act.init_date
        program["hasta fecha"] = Act.end_date
        program["Nombre y Firma del Declarante"] = Organization.representator_name
        program["DNICIF"] = Organization.representator_dni 
        for i in range(len(Act.songs)):
            act_title = str(str(i+1) + " 1")
            act_compositor = str("C")
            if i+1 != 1:
                act_compositor = str(act_compositor + "_" + str(i+1))
            act_subtitle = str(str(i+1) + " 2")
            act_orchestra = str("O")
            if i+1 != 1:
                act_orchestra = str(act_orchestra + "_" + str(i+1))
            act_times = str(i+1)
            if i+1 > 15:
                act_times = str(str(i-14) + "_2")
            if Act.songs[i].title is not None:
                 program[act_title] = Act.songs[i].title
            if Act.songs[i].author is not None:
                 program[act_compositor] = Act.songs[i].author
            if Act.songs[i].subtitle is not None:
                 program[act_subtitle] = Act.songs[i].subtitle
            if Act.songs[i].orchestra is not None:
                 program[act_orchestra] = Act.songs[i].orchestra
            if Act.songs[i].times is not None:
                 program[act_times] = Act.songs[i].times
        self.data_list.append(program)

    # One for each team, registering a file
    def collect_Autoliquidation_data(self, autoliquidation: Autoliquidation, organization: Organization):
        program = Objects().get_Autoliquidacio()
        if autoliquidation.audition_days is not None:
            program["DiesAudicio" ] = autoliquidation.audition_days
        if autoliquidation.audition_price is not None:
            program["PreuAudicio"] = autoliquidation.audition_price
        if autoliquidation.contest_days is not None:
            program["DiesConcurs"] = autoliquidation.contest_days
        if autoliquidation.num_couplets is not None:
            program["NombreDeCobles"] = autoliquidation.num_couplets
        if autoliquidation.concert_days is not None:
            program["DiesConcert"] = autoliquidation.concert_days
        if autoliquidation.concert_earnings is not None:
            program["RecaptacioConcert"] = autoliquidation.concert_earnings
        for i in range(len(autoliquidation.acts)):
            D = str("D" + str(i))
            Full = str("FullN" + str(i))
            program[D] = autoliquidation.acts[i].init_date.split("/")[0]
            program[Full] = autoliquidation.acts[i].number
        if organization.representator_dni is not None:
            program["NIF"] = organization.representator_dni
        if organization.name is not None:
            program["Agrupacio"] = organization.name
        if organization.direction is not None:
            program["Adreça"] = organization.direction
        if organization.city is not None:
            program["Població"] = organization.city
        if organization.postal_code is not None:
            program["CodiPostal"] = organization.postal_code
        if organization.mobile is not None:
            program["Telf"] = organization.mobile
        if organization.place is not None:
            program["Lloc"] = organization.place
        self.data_list.append(program)
    
    # One for all team, registering one entry
    def collect_XLSX_data(self, Organization: Organization):
        template = Objects().get_XLSX()

        with open(os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','XLSX',str(Organization.name) +'.csv')), 'w', newline='') as csvfile:
            fieldnames = ['H. PROGRAMA', 'NOM ORQUESTRA O COBLA', 'DATA INICI', 'DATA FI', 'POBLACIÓ', 'PROVÍNCIA',
                        'LOCAL /CARRER/ESPAI', 'ESDEVENIMENT', 'NOM ENTITAT AUTOLIQUIDACIÓ']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(len(Organization.acts)):
                program = template
                print(Organization.acts[i].init_date)
                program['H. PROGRAMA'] = str("---")
                program['NOM ORQUESTRA O COBLA'] = Organization.name
                program['DATA INICI'] = Organization.acts[i].init_date
                program['DATA FI'] = Organization.acts[i].end_date
                program['POBLACIÓ'] = Organization.acts[i].city
                program['PROVÍNCIA'] = Organization.acts[i].province
                program['LOCAL /CARRER/ESPAI'] = Organization.acts[i].local_name
                program['ESDEVENIMENT'] = Organization.acts[i].title
                program['NOM ENTITAT AUTOLIQUIDACIÓ'] = Organization.acts[i].title
                print(program)
                writer.writerow(program)
                # self.data_list.append(program)

    def write_to_csv(self, file_path):
        df = pd.DataFrame(self.data_list)
        df.to_csv(file_path, index=False)
        print(f'CSV file has been created and saved at: {file_path}')

# Example usage
if __name__ == "__main__":
    csv_writer = CSVWriter()
    song1 = Song("the second", "idk", "subtit", "testing","34")
    song2 = Song("the first", "author1", "Subtit", "Testing", "30")
    act = Act("1","Testing", "Test_name", "Barcelona", "Barcelona", "26/11/2023", "30/11/2023", [song1,song2])
    act2 = Act("1","Testing2", "Test_name", "Barcelona", "Barcelona", "26/11/2023", "30/11/2023", [song1,song2])
    org = Organization([act,act2],"2","Testing_Orchestra","Test","Barcelona","Barcelona","Barcelona","Barcelona","Marc","Rambles","34","fake@mail.com","6543490","2344535","23/11/2023","30/11/2023","fake_dni")
    autoliq = Autoliquidation("28/12/23","50€","29/12/23","30€","4","12","4€",[act,act2])
    csv_writer.collect_Autoliquidation_data(autoliq,org)
    file_path = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Autoliquidations','Testing_Orchestra.csv'))
    csv_writer.write_to_csv(file_path)
