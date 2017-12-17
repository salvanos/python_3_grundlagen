import shutil
import os.path

ori='/Python34/workspace/bmi.txt'
kopie='/Python34/workspace/kopie.txt'

if os.path.exists(ori):
    print('Original existiert')
else:
    print('Original existiert nicht')
if os.path.exists(kopie):
    print('Kopie existiert')
else:
    print('Kopie existiert nicht')
    
shutil.move(ori,kopie)

if os.path.exists(ori):
    print('Original existiert')
else:
    print('Original existiert nicht')
if os.path.exists(kopie):
    print('Kopie existiert')
else:
    print('Kopie existiert nicht')
    

