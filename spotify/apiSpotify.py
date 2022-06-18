import requests
import base64
#https://developer.spotify.com/console/get-search-item/
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQBtiVXki5vEIbYVo6QHXdrCifU0gX_281OwSxoIx5wHiHWZsiY9YfcnavM_G33MnpADEUVTH57fUZ1SoL5gGzlQwjizkkepadK7j8L7R4QlR48WD4zbmTrD4_cFRuFN0qEnHhSSRDO_z2cryuQg2hlnLtGb-9WzedA03Ei2uBiShCE6r0hfyX7rf01G-CE56u066Kmgjf948eIz6RHs4ADLYjg4ITcbP7dTLts85TR_khRueIUcSLlT3w',
}


client_id = 'ad15e2f7f6824d4881a530fbdbd1d130'
client_secret = 'b90edd733aed4948b45c51a41e6dabed'
refresh_token = 'AQANvyrQjZNo3MvCWB1w0WTydvwP2r87e8XGDrRMYdsrhCBKFWKrlCpArk293X3rLFdIP0nAXDm2WznOBhbr9hSl79PpWo9odBprAi29mMnSqgs5iKECeZb0kOs2c3X0QWU'

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
newAccessToken=renovearToken()
print(newAccessToken)
