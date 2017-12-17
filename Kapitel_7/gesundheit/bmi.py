import sqlite3
import os.path

class Benutzer:
    def __init__(self,name,groesse):
        self.name=name
        self.groesse=groesse
class Bmirechner:
    def __init__(self):
        self.datenspeicher={}
        if not os.path.exists('bmi.db'):
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            cursor.execute('''CREATE TABLE bmirechner(name TEXT, bmi REAL)''')
        else:
            connection=sqlite3.connect('bmi.db')
            cursor=connection.cursor()
            cursor.execute('''SELECT name,bmi FROM bmirechner''')
            rows=cursor.fetchall()
            for row in rows:
                name=row[0]
                bmi=row[1]
                if name in self.datenspeicher:
                    bmis=self.datenspeicher[name]
                else:
                    bmis=[]
                bmis.append(bmi)
                self.datenspeicher.update({name:bmis})
    def rechnen(self,gr,ge):
        return round(float(ge)/(float(gr)**2),2)
    def auswerten(self,b):
        if b>=25:
            return 'Übergewicht'
        elif b<18.5:
            return 'Untergewicht'
        else:
            return 'Normalgewicht'
    def hinzufuegen(self,n,b):
        if n in self.datenspeicher:
            bmis=self.datenspeicher[n]
        else:
            bmis=[]
        bmis.append(b)
        self.datenspeicher.update({n:bmis})
        connection=sqlite3.connect('bmi.db')
        cursor=connection.cursor()
        cursor.execute('''INSERT INTO bmirechner VALUES(?,?)''',(n,b))
        connection.commit()
        connection.close()
