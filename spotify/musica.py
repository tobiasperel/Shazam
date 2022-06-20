from spotify.baseDeDatos import insertarCancion,estaLaCancion,agregarReproducciones
from spotify.apiSpotify import agregarALaPlaylist


def agregarCancion(cancion,artista):
    esta = estaLaCancion(cancion ,artista)
    if esta == False:
        agregarALaBaseDeDatos(cancion,artista)
        agregarALaPlaylist(cancion,artista)
    else:
        agregarReproducciones(cancion,artista)

def agregarALaBaseDeDatos(cancion,artista):
    insertarCancion(cancion,artista)


#agregarCancion("Holdg Heart","Genesis")