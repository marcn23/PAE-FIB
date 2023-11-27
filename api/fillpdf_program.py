import pandas as pd
import os
from PyPDF2 import PdfMerger, PdfWriter, PdfReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


def set_need_appearances_writer(writer: PdfWriter):
    try:
        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})
        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

if __name__ == '__main__':
    pdf_filename = "Programa2.pdf"
    csv_filename = "output.csv"
    
    pdfin = os.path.normpath(os.path.join(os.getcwd(),'in',pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(),'out'))
    if not os.path.exists(pdfout):
        # If it doesn't exist, create the directory and any intermediate directories
        os.makedirs(pdfout)

    csvin = os.path.normpath(os.path.join(os.getcwd(),'in',csv_filename))
    
    data = pd.read_csv(csvin)

    pdf = PdfReader(open(pdfin, "rb"), strict=False)  
    if "/AcroForm" in pdf.trailer["/Root"]:
        pdf.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_fields = pdf.get_fields()
    
    csv_fields = data.columns.tolist()
    i = 0 #Filename numerical prefix
    for j, rows in data.iterrows():
        i += 1   
        pdf2 = PdfWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        # Key = pdf_field_name : Value = csv_field_value
        field_dictionary_1 = {}
        keys = ["Nº programa", "título del espectáculo", "Valoración del Programa",
        "Orquesta o cobla", "Evento n", "Local", "Cód Local", "Pedido n",
        "Domicilio", "Factura n", "Población", "Provincia", "Incluido en liquidación",
        "N de hojas", "Nombre del declarante", "N de títulos", "Partes",
        "Dirección", "CP", "Población_2", "Provincia_2", "Correo electrónico",
        "D", "Teléfono", "Código socio SGAE", "Titular de Zona N", "Fecha",
        "de", "año", "desde fecha", "hasta fecha","1 1", "C", "1 2", "O", "1", 
        "2 1", "C_2", "2 2", "O_2", "2","3 1", "C_3", "3 2", "O_3", "3", "4 1", "C_4", "4 2", "O_4", "4",
        "5 1", "C_5", "5 2", "O_5", "5", "6 1", "C_6", "6 2", "O_6", "6",
        "7 1", "C_7", "7 2", "O_7", "7", "8 1", "C_8", "8 2", "O_8", "8",
        "9 1", "C_9", "9 2", "O_9", "9", "10 1", "C_10", "10 2", "O_10", "10",
        "11 1", "C_11", "11 2", "O_11", "11", "12 1", "C_12", "12 2", "O_12", "12",
        "13 1", "C_13", "13 2", "O_13", "13", "14 1", "C_14", "14 2", "O_14", "14",
        "15 1", "C_15", "15 2", "O_15", "15", "16 1", "C_16", "16 2", "O_16", "1_2",
        "17 1", "C_17", "17 2", "O_17", "2_2", "18 1", "C_18", "18 2", "O_18", "3_2",
        "19 1", "C_19", "19 2", "O_19", "4_2", "20 1", "C_20", "20 2", "O_20", "5_2",
        "21 1", "C_21", "21 2", "O_21", "6_2", "22 1", "C_22", "22 2", "O_22", "7_2",
        "23 1", "C_23", "23 2", "O_23", "8_2", "24 1", "C_24", "24 2", "O_24", "9_2",
        "25 1", "C_25", "25 2", "O_25", "10_2", "26 1", "C_26", "26 2", "O_26", "11_2",
        "27 1", "C_27", "27 2", "O_27", "12_2", "28 1", "C_28", "28 2", "O_28", "13_2",
        "29 1", "C_29", "29 2", "O_29", "14_2", "30 1", "C_30", "30 2", "O_30", "15_2","Nombre y Firma del Declarante","DNICIF"]
        for key in keys:
            if rows[key] != "---":
                field_dictionary_1[key] = rows[key]
            else:
                print("Not valid")

        temp_out_dir = os.path.normpath(os.path.join(pdfout,str(rows['Orquesta o cobla']) + '_Programa.pdf'))
        pdf2.add_page(pdf.pages[0])
        pdf2.add_page(pdf.pages[1])
        pdf2.update_page_form_field_values(pdf2.pages[0], field_dictionary_1)
        pdf2.update_page_form_field_values(pdf2.pages[1], field_dictionary_1)
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream)
        outputStream.close()
        
        teorical_extra_sheet = os.path.normpath(os.path.join(os.getcwd(),'in','Repertoris',str(rows['Orquesta o cobla']) + '_Repertori.pdf'))
        print(teorical_extra_sheet)
        if os.path.exists(teorical_extra_sheet): 
            merger = PdfMerger()
    
            merger.append(PdfReader(open(temp_out_dir, 'rb')))
            merger.append(PdfReader(open(teorical_extra_sheet, 'rb')))
            
            merger.write(temp_out_dir)
    
    print(f'El·laboracio d\'arxius finalitzada')