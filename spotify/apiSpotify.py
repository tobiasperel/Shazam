import requests
import base64
try:
    from spotify.keysSpotify import *
except:
    from keysSpotify import *
#https://developer.spotify.com/console/get-search-item/

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer' + ' ' + bareerToken,
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
    try:
        response = requests.get('https://api.spotify.com/v1/search', params=params, headers=headers)
        data = response.json()
        listaDeArtitstas = data["tracks"]["items"]
    except:
        headers["Authorization"] = 'Bearer' + ' ' + renovearToken()
        return -1
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
    if idCancion == -1:
        idCancion= obtenerId(cancion,artista)
    if idCancion != 0:
        respuesta = addItemToAPlaylist(idCancion)
        print(respuesta)

def renovearToken():
    
    url = 'https://accounts.spotify.com/api/token'
    headers1 = {'Authorization': 'Basic ' + base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')}
    form = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}

    response = requests.post(url, data=form, headers=headers1)
    data = response.json()
    return data["access_token"]

#agregarALaPlaylist("Paradise","Coldplay")
#newAccessToken=renovearToken()
#print("Bearer", newAccessToken)
