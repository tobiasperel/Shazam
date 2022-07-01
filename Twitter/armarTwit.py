from datetime import datetime

def armarTwit(cancion, artista):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    hora = str(int(current_time.split(":")[0])-3)
    if int(hora) < 0:
        hora +=  3
    current_time.split(":")[0] = hora
    current_time = hora + ":" + current_time.split(":")[1] + ":" + current_time.split(":")[2]
    text = "Hoy, a las " + current_time + ", La cancion " + cancion + " del artista " + artista + " sono en Aspen."
    return text
