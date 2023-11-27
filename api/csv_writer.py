import string
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
        #TODO
        return False
    
    # One for all team, registering one entry
    def collect_XLSX_data(self):
        #TODO
        return False

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
