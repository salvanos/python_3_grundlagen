import os.path
import time

p='/Python34/workspace/bmi.txt'

if os.path.exists(p):
    print('Existiert')
    if os.path.isfile(p):
        print('Ist eine Datei')
        print('Größe:',os.path.getsize(p))
        print('Änderungsdatum:'+time.ctime(os.path.getmtime(p)))
