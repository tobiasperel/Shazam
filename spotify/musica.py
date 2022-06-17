from spotify.baseDeDatos import insertarCancion, pasarTablaADiccionario,estaLaCancion

cancionesYArtistas = pasarTablaADiccionario()
print(cancionesYArtistas)

def agregarCancion(cancion,artista):
    try:
        esta = estaLaCancion(cancion ,artista)
    except Exception as e:
        print(e)
        esta = True
    if esta == False:
        agregarALaBaseDeDatos(cancion,artista)

def agregarALaBaseDeDatos(cancion,artista):
    try:
        insertarCancion(cancion,artista)
    except Exception as e:
        print(e)

agregarCancion("Holdg Heart","Genesis")