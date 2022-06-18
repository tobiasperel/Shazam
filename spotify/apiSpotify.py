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
    'Authorization': 'Bearer BQBhBQyqaTQArzQW678Ysyqza9cTtLLNhsaT2wFsgdCQ4Hri14WDbJhIZQLJVgCbsnWezdV3v1PYbAVwCehowXKr8WHxbqHLxgfo9jHpzZEJA9MM5jd5YHM3qaTCBtrR8_Eu0PGl4HtAevxK79ERgYBWB-MDZCGj1Ju7fRkN-VZjr_PjOmeR7NigZ2tiUUeaFCyckQtqhOJG83_omH0eEBeuK-Vj8JGMsbiuO07vUQQP627ODUftQz2-8',
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

def renovearToken():
    
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': 'Basic ' + base64.b64encode(bytes(client_id + ':' + client_secret, 'utf-8')).decode('utf-8')}
    form = {'grant_type': 'refresh_token', 'refresh_token': refresh_token}

    response = requests.post(url, data=form, headers=headers)
    data = response.json()
    return data["access_token"]

#agregarALaPlaylist("I cant dance","Genesis")
#newAccessToken=renovearToken()
#print(newAccessToken)
