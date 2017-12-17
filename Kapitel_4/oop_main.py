class Benutzer:
    name=''
    groesse=0.0
    def anmelden(self):
        print('Anmeldung Benutzer:',self.name)
    def __init__(self,name,groesse):
        self.name=name
        self.groesse=groesse
        print('Ich werde initialisiert')
    def __del__(self):
        print('Ich werde gelöscht')
    def __str__(self):
        return 'Benutzer:'+self.name
class Administrator(Benutzer):
    def __init__(self,name,groesse,kennwort):
        self.name=name
        self.groesse=groesse
        self.kennwort=kennwort
        print('Ich werde initialisiert')
    def __str__(self):
        return 'Benutzer:'+self.name+' hat das Kennwort'+self.kennwort
benutzer1=Benutzer('Alex',1.75)
benutzer1.anmelden()
print(benutzer1)
benutzer2=Administrator('Pinki',0.6,'Taxi#750')
print(benutzer2)
