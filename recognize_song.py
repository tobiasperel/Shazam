import asyncio
from shazamio import Shazam
import tweepy
from keys import *
from datetime import datetime
import time 
from radio import grabar
client = tweepy.Client(consumer_key= consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

# Replace the text with whatever you want to Tweet about

async def main():
    shazam = Shazam()
    out = await shazam.recognize_song('output.wav')
    try:
        cancion = out["track"]["title"]
        artista = out["track"]["subtitle"]
    except:
        return ("No se pudo reconocer la cancion", "")
    print(cancion)  
    print(artista) 
    return (cancion, artista)

def averiguarCancion(): 
    loop = asyncio.get_event_loop()
    cancion, artista = loop.run_until_complete(main())
    return (cancion, artista)

def escribirTweet(text):
    client.create_tweet(text=text)

cancionVieja = ""
artistaViejo = ""
grabar()
while True:
    cancion, artista = averiguarCancion()
    if cancion == "No se pudo reconocer la cancion":
        print("No se pudo reconocer la cancion")
        time.sleep(60)
        grabar()
        continue
    if cancion == cancionVieja and artista == artistaViejo:
        time.sleep(120)
        grabar()
        continue
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text = "Hoy, a las " +current_time+ ", La cancion " + cancion + " del artista " + artista + " esta sonando en aspen."
    escribirTweet(text)
    cancionVieja = cancion
    artistaViejo = artista