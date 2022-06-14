from spotify.baseDeDatos import insertarCancion
cancionesYArtistas = {}

def agregarCancion(cancion,artista):
    canciones = list(cancionesYArtistas.values())
    if cancion not in canciones:
        canciones.append(cancion)
        cancionesYArtistas[artista] = cancion
    print(cancionesYArtistas)
    insertarCancion(cancion,artista)

