import os
import pandas as pd

class Testing():

    ##Constructor
    def __init__(self, filepath, createPathToSave, fileName):
        self.filepath = filepath;
        self.createPathToSave = createPathToSave;
        self.fileName = fileName;

    ##Read csv file from local directory
    def readCSV(self):
        with open(self.filepath, 'r') as csv_file:
            
            txt = pd.read_csv(csv_file);
            return txt;

    ##Add boolean flag to tell if expired
    def addNewColAndFlag(self, csvfile):
        csvfile["obsolete"] = pd.to_datetime(csvfile["date"], format='%Y-%m-%d') <  pd.to_datetime("2021-01-01", format='%Y-%m-%d');
        return csvfile;

    ##Convert csv file to json
    def convToJson(self, csvfile):
        return csvfile.to_json(orient='records')

    ##Save to the local directory
    def Save(self, jsonObj):
        os.mkdir(self.createPathToSave);
        completeFileDir = os.path.join(self.createPathToSave, self.fileName)  
        f = open(completeFileDir, "w");
        f.write(jsonObj);
        f.close;
        print("Saved!")        

##TESTING

##INSTANTIATING CLASS
p1 = Testing('C:/python-hands-on-dataset.csv', 'C:/Test/', 'python-hands-on-dataset.json');

##READING CSV
t = p1.readCSV()

##ADDING EXPIRED FLAG
u = p1.addNewColAndFlag(t);

##CONVERTING TO JSON
v = p1.convToJson(u);

##SAVING..
w = p1.Save(v);
   
