import pandas as pd
import os
from PyPDF2 import PdfWriter, PdfReader
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
    # csv_filename = "data.csv"
    pdf_filename = "SGAE.pdf"
    csv_filename = "okData.csv"
    # pdf_filename = "EIS 3 Certificate - Autofilled.pdf"

    # csvin = os.path.normpath(os.path.join(os.getcwd(),'in',csv_filename))
    pdfin = os.path.normpath(os.path.join(os.getcwd(),'in',pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(),'out'))
    csvin = os.path.normpath(os.path.join(os.getcwd(),'in',csv_filename))
    data = pd.read_csv(csvin)

    # print(data.columns[0])

    pdf = PdfReader(open(pdfin, "rb"), strict=False)  
    if "/AcroForm" in pdf.trailer["/Root"]:
        pdf.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_fields = pdf.get_fields()
    #pdf_fields = [str(x) for x in pdf.get_fields().keys] # List of all pdf field names
    csv_fields = data.columns.tolist()
    # print(pdf_fields)
    #print(csv_fields)
    i = 0 #Filename numerical prefix
    for j, rows in data.iterrows():
        i += 1   
        pdf2 = PdfWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        # Key = pdf_field_name : Value = csv_field_value
        
        field_dictionary_1 = {
        "Audicions i/o ballades: Dies": rows['DiesAudicio'],
        "Audicions i/o ballades a": rows['PreuAudicio'],
        "Audicions i/o ballades a: €:": "?",
        "Nombre de cobles: €": str("?"),
        "Concursos de sardanes: Dies": rows['DiesConcurs'],
        "Nombre de cobles": rows['NombreDeCobles'],
        "Si és gratuit:": rows['RecaptacioConcert'],
        "Aplecs i/o concerts: Dies": rows['DiesConcert'],
        "Si és gratuit: €": "?",
        "Si hi ha recaptació: 10% s/taquilla": str("?"),
        "Si hi ha recaptació: 10% s/taquilla: €": str("?"),
        "Base imposable: €": str("?"),
        "TOTAL A PAGAR: €": str("?"),
        "nombre": str("where?"),
        "Dia-1:": rows['D1'],
        "Full núm-1:": rows['FullN1'],
        "Dia-2:": rows['D2'],
        "Full núm-2:": rows['FullN2'],
        "Dia-3:": rows['D3'],
        "Full núm-3:": rows['FullN3'],
        "Dia-4:": rows['D4'],
        "Full núm-4:": rows['FullN4'],
        "Dia-5:": rows['D5'],
        "Full núm-5:": rows['FullN5'],
        "Dia-6:": rows['D6'],
        "Full núm-6:": rows['FullN6'],
        "Dia-7:": rows['D7'],
        "Full núm-7:": rows['FullN7'],
        "Dia-8:": rows['D8'],
        "Full núm-8:": rows['FullN8'],
        "Dia-9:": rows['D9'],
        "Full núm-9:": rows['FullN9'],
        "Dia-10:": rows['D10'],
        "Full núm-10:": rows['FullN10'],
        "NIF:": rows['NIF'],
        "Agrupació sardanista:": rows['Agrupacio'],
        "Adreça:": rows['Adreça'],
        "Polbació:": rows['Població'],
        "Codi Postal:": rows['CodiPostal'],
        "Telèfon:": rows['Telf'],
        "A:": rows['Lloc'] }

        temp_out_dir = os.path.normpath(os.path.join(pdfout,str(i) + 'out.pdf'))
        pdf2.add_page(pdf.pages[0])
        pdf2.update_page_form_field_values(pdf2.pages[0], field_dictionary_1)
        # pdf2.add_page(pdf.pages[1])
        # pdf2.add_page(pdf.pages[2])
        # pdf2.add_page(pdf.pages[3])
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream)
        outputStream.close()
    print(f'Process Complete: PDFs Processed!')