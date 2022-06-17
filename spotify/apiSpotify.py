import requests

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQANybyxb26om0lgNMK2A4ERWQigJhWGoYZGNV23-iZKF1ZRY9PAgPYLgBx5RV7DclSa0tXl6wXyglwkeA_885s_HZMPoPL6wsWzSVqoCrXIWML8jKNTEWEtSV6wEG0hEH4mn5-XoLJrkk9Y4DSm6CCx7lUw7e8c5gU-oNKOs9rPMk-4uRsIq_IsnUYDFdW3oWY4GPL_DV0DcSAtIGRCT8sSUfU7uRItAdaW_V7i4iGAndpRx7mfxsECag',
}

def addItemToAPlaylist(idCancion):

    params = {
        'uris': 'spotify:track:' + idCancion,
    }

    response = requests.post('https://api.spotify.com/v1/playlists/7xYES5FHi7fDmsWjp56GWy/tracks', params=params, headers=headers)
    return response.json()

def obtenerId(cancion,artistaBDD):
    
    params = {
        'q': cancion, 
        'type': 'track',
    }
    response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
    data = response.json()
    listaDeArtitstas = data["tracks"]["items"]
    idCancion = 0
    for artistaYMuchasCosas in listaDeArtitstas:
        artistaSpotify = artistaYMuchasCosas["artists"][0]["name"]
        if artistaSpotify == artistaBDD:
            idCancion = artistaYMuchasCosas["id"]
            print(cancion , artistaSpotify)
            return idCancion
    return idCancion


def agregarALaPlaylist(cancion,artista):
    idCancion= obtenerId(cancion,artista)
    if idCancion != 0:
        respuesta = addItemToAPlaylist(idCancion)
        print(respuesta)

#agregarALaPlaylist("I cant dance","Genesis")