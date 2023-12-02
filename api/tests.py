import pandas as pd
import os
import time
import subprocess
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from classes.Act import Act
from classes.Organization import Organization
from classes.Songs import Song
from classes.Autoliquidation import Autoliquidation
from csv_writer import CSVWriter

if __name__ == '__main__':

    song1 = Song("the second", "idk", "subtit", "testing","34")
    song2 = Song("the first", "author1", "Subtit", "Testing", "30")
    act = Act("1","Testing", "Test_name", "Barcelona", "Barcelona", "26/11/2023", "30/11/2023", [song1,song2])
    act2 = Act("1","Testing2", "Test_name", "Barcelona", "Barcelona", "26/11/2023", "30/11/2023", [song1,song2])
    org = Organization([act,act2],"2","Testing_Orchestra","Test","Barcelona","Barcelona","Barcelona","Barcelona","Marc","Rambles","34","fake@mail.com","6543490","2344535","23/11/2023","30/11/2023","fake_dni")
    autoliquidation = Autoliquidation("26/11/2023","30€", None, None, None, "26/11/2023", "300€", [act,act2])
    
    csv_writer = CSVWriter()
    csv_writer.collect_XLSX_data(org)
    file_path = 'output.csv'
    csv_writer.write_to_csv(file_path)


    cs3 = CSVWriter()
    cs3.collect_SGAE_data(org, act)
    file_path1 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Programs',str(org.name) +'.csv'))
    cs3.write_to_csv(file_path1)

    cs2 = CSVWriter()
    cs2.collect_Autoliquidation_data(autoliquidation,org)
    file_path2 = os.path.normpath(os.path.join(os.getcwd(),'in','CSVs','Autoliquidations',str(org.name) +'.csv'))
    cs2.write_to_csv(file_path2)

    time.sleep(2)
    try:
        result = subprocess.run(['python', "fillpdf.py", "Testing_Orchestra"])
        result = subprocess.run(['python', "fillpdf_program.py", "Testing_Orchestra"])
        result = subprocess.run(['python', "fillxlsx.py", "Testing_Orchestra"])
    except Exception as e:
        print(f"Error executing the script: {e}")
