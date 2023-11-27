import os
import csv
import pandas as pd
from classes.objectInstances import Objects
from classes.Organization import Organization
from classes.Act import Act
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
        print("out")
        for i in range(len(Act.songs)):
            print("OK")
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
    def collect_Autoliquidation_data(self):
        # program = Objects().get_Autoliquidacio()
        # D1
        # FullN1
        # D2
        # FullN2
        # D3
        # FullN3
        # D4
        # FullN4
        # D5
        # FullN5
        # D6
        # FullN6
        # D7
        # FullN7
        # D8
        # FullN8
        # D9
        # FullN9
        # D10
        # FullN10
        # NIF
        # Agrupacio
        # Adreça
        # Població
        # CodiPostal
        # Telf
        # Lloc
        return 
    
    # One for all team, registering one entry
    def collect_XLSX_data(self, Organization: Organization):
        program = Objects().get_XLSX()

        with open(os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','XLSX',str(Organization.name) +'_XLSXinput.csv')), 'w', newline='') as csvfile:
            fieldnames = ['H. PROGRAMA', 'NOM ORQUESTRA O COBLA', 'DATA INICI', 'DATA FI', 'POBLACIÓ', 'PROVÍNCIA',
                        'LOCAL /CARRER/ESPAI', 'ESDEVENIMENT', 'NOM ENTITAT AUTOLIQUIDACIÓ']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for i in range(len(Organization.acts)):
                program['H. PROGRAMA'] = str("---")
                program['NOM ORQUESTRA O COBLA'] = Organization.name
                program['DATA INICI'] = Organization.acts[i].init_date
                program['DATA FI'] = Organization.acts[i].end_date
                program['POBLACIÓ'] = Organization.acts[i].city
                program['PROVÍNCIA'] = Organization.acts[i].province
                program['LOCAL /CARRER/ESPAI'] = Organization.acts[i].local_name
                program['ESDEVENIMENT'] = Organization.acts[i].title
                program['NOM ENTITAT AUTOLIQUIDACIÓ'] = Organization.acts[i].title

                writer.writerow(program)

    def write_to_csv(self, file_path):
        df = pd.DataFrame(self.data_list)
        df.to_csv(file_path, index=False)
        print(f'CSV file has been created and saved at: {file_path}')

# Example usage
if __name__ == "__main__":
    csv_writer = CSVWriter()
    csv_writer.collect_SGAE_data()
    #TODO: change name
    file_path = 'output.csv'
    csv_writer.write_to_csv(file_path)
