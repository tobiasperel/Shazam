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
        try:
            escribirTweet(text)
        except:
            escribirTweet(text)
        cancionVieja = cancion
        artistaViejo = artista

if __name__ == "__main__":
    try:
        main()
    except:
        send_message()