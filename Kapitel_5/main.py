#!/usr/bin/python
from gesundheit.bmi import Benutzer,Bmirechner

benutzer=Benutzer()
bmirechner=Bmirechner()
while True:
    try:
        bmi=bmirechner.rechnen(benutzer.groesse)
        if not bmi:
            break
    except ValueError:
        continue
    bmirechner.auswerten(bmi)
    bmirechner.hinzufuegen(benutzer.name,bmi)
bmirechner.ausgeben()

