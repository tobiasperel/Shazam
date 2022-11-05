from apiSpotify import *
from baseDeDatos import obtenerCancionesYartista

print(obtenerId("Paradise","Coldplay"))
mensaje = "spotify:track:"
#mensaje += obtenerId("Paradise","Coldplay") + ","
#mensaje += obtenerId("clocks","Coldplay") + ","
#print(mensaje[:-1]) # a partir de la 962

data = obtenerCancionesYartista(962)
#print(data[0][0])
#print(len(data))

for i in range(len(data)):
    cancion = data[i][0]
    artista = data[i][1]
    id = obtenerId(cancion,artista)
    if id == 0:
        continue
    mensaje += str(id) + ",spotify:track:" 
    #time.sleep(1)
print(mensaje)