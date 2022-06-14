from spotify.baseDeDatos import insertarCancion, pasarTablaADiccionario

cancionesYArtistas = pasarTablaADiccionario()
print(cancionesYArtistas)

def agregarCancion(cancion,artista):
    canciones = list(cancionesYArtistas.values())
    if cancion not in canciones:
        cancionesYArtistas[artista] = cancion
        print(cancionesYArtistas)
        try:
            insertarCancion(cancion,artista)
        except Exception as e:
            print(e)

