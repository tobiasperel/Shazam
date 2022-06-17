import asyncio
from shazamio import Shazam

async def GeneralShazam():
    shazam = Shazam()
    out = await shazam.recognize_song('output.wav')
    try:
        cancion = out["track"]["title"]
        artista = out["track"]["subtitle"]
    except:
        return ("No se pudo reconocer la cancion", "")
    #print(cancion)  
    #print(artista) 
    return (cancion, artista)

def averiguarCancion(): 
    loop = asyncio.get_event_loop()
    cancion, artista = loop.run_until_complete(GeneralShazam())
    return (cancion, artista)