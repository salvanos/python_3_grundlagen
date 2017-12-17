datei=open(p,'w')
datei.write('Pinki')
datei.close()

datei=open(p)
zeile=datei.readline()
print(zeile)
datei.close()



