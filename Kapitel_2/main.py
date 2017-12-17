#!/usr/bin/python
''' main - ein kleines Beispielprogramm '''

name=input('Name:')
print('Hallo',name)
groesse=input('Körpergröße:')

datenspeicher={}
while True:
    gewicht=input('Gewicht:')
    if not gewicht:
        break
    try:
        bmi=round(float(gewicht)/(float(groesse)**2),2)
    except ValueError:
        continue
    print('BMI:',bmi)
    if bmi>=25:
        print('Übergewicht')
    elif bmi<18.5:
        print('Untergewicht')
    else:
        print('Normalgewicht')
    if name in datenspeicher:
        bmis=datenspeicher[name]
    else:
        bmis=[]
    bmis.append(bmi)
    datenspeicher.update({name:bmis})
for i in datenspeicher.items():
    print(i)


