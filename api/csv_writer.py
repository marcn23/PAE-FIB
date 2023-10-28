import string
import pandas as pd
from classes.objectInstances import Objects
from classes.Organization import Organization

class CSVWriter:
    def __init__(self):
        self.data_list = []

    # One for each team, registering a file
    def collect_SGAE_data(self, Organization: Organization):
        tst = Objects()
        tst.get()
        tst.data["Nº programa"] = ""
        for i in range(len(Organization.acts)):
            act_title = string(i+1 + " 1")
            act_compositor = string("C")
            if i+1 != 1:
                act_compositor = string(act_compositor + "_" + i+1)
            act_subtitle = string(i+1 + " 2")
            act_orchestra = string("O")
            if i+1 != 1:
                act_orchestra = string(act_orchestra + "_" + i+1)
            if i+1 > 15:
                act_times = string((i-14) + "_2")
            else: 
                act_times = string(i+1)

            if Organization.acts[i].title is not None:
                 tst.data[act_title]: Organization.acts[i].title
            if Organization.acts[i].author is not None:
                 tst.data[act_compositor]: Organization.acts[i].author
            if Organization.acts[i].subtitle is not None:
                 tst.data[act_subtitle]: Organization.acts[i].subtitle
            if Organization.acts[i].orchestra is not None:
                 tst.data[act_orchestra]: Organization.acts[i].orchestra
            if Organization.acts[i].times is not None:
                 tst.data[act_times]: Organization.acts[i].times
        self.data_list.append(tst.data)

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
