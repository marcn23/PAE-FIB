import pandas as pd
import os
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
from classes.Act import Act
from classes.Organization import Organization
from classes.Songs import Song
from csv_writer import CSVWriter

if __name__ == '__main__':

    song1 = Song("the second", "idk", "subtit", "testing","34")
    song2 = Song("the first", "author1", "Subtit", "Testing", "30")
    act = Act("Testing", "Test_name", "Barcelona", "Barcelona", "26/11/2023", "30/11/2023", [song1,song2])
    org = Organization(act,"2","Testing_Orchestra","Test","Barcelona","Barcelona","Barcelona","Barcelona","Marc","Rambles","34","fake@mail.com","6543490","2344535","23/11/2023","30/11/2023","fake_dni")
    
    cs = CSVWriter()
    cs.collect_SGAE_data(org, act)
    file_path = os.path.normpath(os.path.join(os.getcwd(),'out','output.csv'))
    cs.write_to_csv(file_path)