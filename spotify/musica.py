from spotify.baseDeDatos import insertarCancion, pasarTablaADiccionario

cancionesYArtistas = pasarTablaADiccionario()
print(cancionesYArtistas)

def agregarCancion(cancion,artista):
    canciones = list(cancionesYArtistas.values())
    if cancion not in canciones:
        if artista in cancionesYArtistas.keys():
            cancionesYArtistas[artista].append(cancion)
        else:
            cancionesYArtistas[artista] = list()
            cancionesYArtistas[artista].append(cancion)
        print(cancionesYArtistas)
        try:
            insertarCancion(cancion,artista)
        except Exception as e:
            print(e)

#agregarCancion("Clocks","Coldplay")

