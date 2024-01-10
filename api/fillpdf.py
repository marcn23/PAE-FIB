import pandas as pd
import os
import sys
from PyPDF2 import PdfMerger, PdfReader, PdfWriter, PdfReader
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
    org = sys.argv[1]
    csv_filename = str(org) + ".csv"
    pdf_filename = "SGAE_Autoliquidation_Template.pdf"
    
    pdfin = os.path.normpath(os.path.join(os.getcwd(),'in',pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(),'out', 'Autoliquidations'))
    if not os.path.exists(pdfout):
        # If it doesn't exist, create the directory and any intermediate directories
        os.makedirs(pdfout)

    csvin = os.path.normpath(os.path.join(os.getcwd(),'in',"CSVs","Autoliquidations",csv_filename))
    
    data = pd.read_csv(csvin)

    pdf = PdfReader(open(pdfin, "rb"), strict=False)  
    if "/AcroForm" in pdf.trailer["/Root"]:
        pdf.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_fields = pdf.get_fields()
    csv_fields = data.columns.tolist()
    i = 0 #Filename numerical prefix
    print(str(pdf_fields))
    for j, rows in data.iterrows():
        i += 1   
        pdf2 = PdfWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        # Key = pdf_field_name : Value = csv_field_value
        field_dictionary_1 = {}
        data = ["Audicions i/o ballades: Dies","Audicions i/o ballades a: €:","Concursos de sardanes: Dies","Nombre de cobles","Si és gratuit: €","Aplecs i/o concerts: Dies","Dia-1:","Full núm-1:","Dia-2:","Full núm-2:","Dia-3:","Full núm-3:","Dia-4:","Full núm-4:","Dia-5:","Full núm-5:","Dia-6:","Full núm-6:","Dia-7:","Full núm-7:","Dia-8:","Full núm-8:","Dia-9:","Full núm-9:","Dia-10:","Full núm-10:","NIF:","Agrupació sardanista:","Adreça:","Polbació:","Codi Postal:","Telèfon:","A:"]
        keys = ["DiesAudicio","PreuAudicio","DiesConcurs","NombreDeCobles","RecaptacioConcert","DiesConcert","D1","FullN1","D2","FullN2","D3","FullN3","D4","FullN4","D5","FullN5","D6","FullN6","D7","FullN7","D8","FullN8","D9","FullN9","D10","FullN10","NIF","Agrupacio","Adreça","Població","CodiPostal","Telf","Lloc"]
        print("other: " + str(len(data)))
        print("Keys: " + str(len(keys)))
        for key in range(len(keys)):
            print("Keys value" + str(keys[key]) + ": " + str(rows[keys[key]]))
            if rows[keys[key]] != "---":
                field_dictionary_1[data[key]] = rows[keys[key]]
            else:
                print("Not valid")

        temp_out_dir = os.path.normpath(os.path.join(pdfout,str(org) + '_Autoliquidacio.pdf'))
        pdf2.add_page(pdf.pages[0])
        pdf2.update_page_form_field_values(pdf2.pages[0], field_dictionary_1)
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream)
        outputStream.close()

        #In case it is needed 
        teorical_extra_sheet = os.path.normpath(os.path.join(os.getcwd(),'in','Repertoris',str(rows['Agrupacio']) + '_Repertori.pdf'))
        print(teorical_extra_sheet)
        if os.path.exists(teorical_extra_sheet): 
            merger = PdfMerger()
    
            merger.append(PdfReader(open(temp_out_dir, 'rb')))
            merger.append(PdfReader(open(teorical_extra_sheet, 'rb')))
            
            merger.write(temp_out_dir)

    print(f'El·laboracio d\'arxius finalitzada')