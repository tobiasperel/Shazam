import asyncio
from shazamio import Shazam
from datetime import datetime
import time 
from radio import grabar
from mandarTweet import escribirTweet

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
    text = "Hoy, a las " +current_time+ ", La cancion " + cancion + " del artista " + artista + " sono en aspen."
    escribirTweet(text)
    cancionVieja = cancion
    artistaViejo = artista