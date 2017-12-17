class Benutzer:
    ''' repräsentiert einen BMI Benutzer '''
    def __init__(self):
        ''' Der Konstruktor des Benutzers '''
        self.name=input('Name:')
        self.groesse=input('Körpergröße:')
class Bmirechner:
    ''' repräsentiert einen BMI Rechner '''
    def __init__(self):
        ''' Der Konstruktor des BMI Rechners '''
        self.datenspeicher={}
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
    def ausgeben(self):
        for i in self.datenspeicher.items():
            print(i)    
