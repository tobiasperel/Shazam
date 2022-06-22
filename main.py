from pandas import ExcelFile
from Twitter.mandarTweet import escribirTweet
from Twitter.armarTwit import armarTwit
from spotify.musica import agregarCancion
from shazam.reconocerCancionShazam import averiguarCancion
from shazam.radio import grabar
import time 
from Telegram.mandarTelegram import send_message

def main():
    cancionVieja = ""
    artistaViejo = ""
    grabar()
    
    while True:
        try:
            cancion, artista = averiguarCancion()
            if cancion == "No se pudo reconocer la cancion":
                time.sleep(60)
                grabar()
                continue
            if cancion == cancionVieja and artista == artistaViejo:
                time.sleep(120)
                grabar()
                continue
            agregarCancion(cancion, artista)
            text = armarTwit(cancion, artista)
            escribirTweet(text)
            cancionVieja = cancion
            artistaViejo = artista
        except:
            continue
    
if __name__ == "__main__":
    main()