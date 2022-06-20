from datetime import datetime

def armarTwit(cancion, artista):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    text = "Hoy, a las " + current_time + ", La cancion " + cancion + " del artista " + artista + " sono en Aspen."
    return text