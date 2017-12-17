import os.path
from ast import literal_eval

class Benutzer:
    def __init__(self):
        self.name=input('Name:')
        self.groesse=input('Körpergröße:')
class Bmirechner:
    def __init__(self):
        self.datenspeicher={}
        if os.path.exists('bmi.txt'):
            datei=open('bmi.txt')
            for zeile in datei:
                parts=zeile.split(':')
                name=parts[0]
                bmis=literal_eval(parts[1])
                self.datenspeicher.update({name:bmis})
            datei.close()
    def rechnen(self,gr):
        gewicht=input('Gewicht:')
        if not gewicht:
            return
        return round(float(gewicht)/(float(gr)**2),2)
    def auswerten(self,b):
        if b>=25:
            print('Übergewicht')
        elif b<18.5:
            print('Untergewicht')
        else:
            print('Normalgewicht')
    def hinzufuegen(self,n,b):
        if n in self.datenspeicher:
            bmis=self.datenspeicher[n]
        else:
            bmis=[]
        bmis.append(b)
        self.datenspeicher.update({n:bmis})
        datei=open('bmi.txt','w')
        for name in self.datenspeicher.keys():
            datei.write(name+':[')
            bmis=self.datenspeicher[name]
            first=True
            for bmi in bmis:
                if not first:
                    datei.write(',')
                datei.write(str(bmi))
                first=False
            datei.write(']\n')
        datei.close()
    def ausgeben(self):
        for i in self.datenspeicher.items():
            print(i)    
