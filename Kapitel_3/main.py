#!/usr/bin/python
''' main - ein kleines Beispielprogramm '''

def rechnen(gr):
    gewicht=input('Gewicht:')
    if not gewicht:
        return
    return round(float(gewicht)/(float(gr)**2),2)
def auswerten(b):
    if b>=25:
        print('Übergewicht')
    elif b<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')
def hinzufuegen(n,b):
    if n in datenspeicher:
        bmis=datenspeicher[n]
    else:
        bmis=[]
    bmis.append(b)
    datenspeicher.update({n:bmis})
def ausgeben():
    for i in datenspeicher.items():
        print(i)    
name=input('Name:')
print('Hallo',name)
groesse=input('Körpergröße:')

datenspeicher={}
while True:
    try:
        bmi=rechnen(groesse)
        if not bmi:
            break
    except ValueError:
        continue
    auswerten(bmi)
    hinzufuegen(name,bmi)
ausgeben()