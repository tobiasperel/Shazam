import sqlite3

try:
    conn = sqlite3.connect('spotify/database.db')
except:
    conn = sqlite3.connect('database.db')
c = conn.cursor()

def iniciarTabla(c):
    c.execute('''CREATE TABLE IF NOT EXISTS "cancionesConReproducciones" 
                ("ID"	INTEGER NOT NULL,
                "cancion"	TEXT,
                "artista"	TEXT,
                "cantidadDeVecesRepoducida"	INTEGER,
                PRIMARY KEY("ID" AUTOINCREMENT)
                );''')
    conn.commit()

def insertarCancion(cancion,artista,cantidadDeVecesRepoducida = 1):
    c.execute(f'''INSERT INTO cancionesConReproducciones (
            cancion,artista,cantidadDeVecesRepoducida)VALUES("{cancion}","{artista}","{cantidadDeVecesRepoducida}")''')
    conn.commit()

def estaLaCancion(cancion, artista, tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f'''SELECT * from {tabla} WHERE cancion = "{cancion}"  AND artista = "{artista}" '''.format(cancion,artista))
    if len(cursor.fetchall()) == 0:
        return False
    return True

def agregarReproducciones(cancion,artista, tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f'''SELECT * from {tabla} WHERE cancion = "{cancion}"  AND artista = "{artista}" '''.format(cancion,artista))
    cantidadDeVecesRepoducida = cursor.fetchall()[0][3]
    cursor = cursor.execute('''UPDATE cancionesConReproducciones SET cantidadDeVecesRepoducida = "{cantidadDeVecesRepoducida}" + 1 where cancion = "{cancion}" AND artista = "{artista}" ''' .format(cantidadDeVecesRepoducida = cantidadDeVecesRepoducida,cancion = cancion,artista = artista))
    conn.commit()

def masReproducidas(tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f'''SELECT * from {tabla} ORDER BY cantidadDeVecesRepoducida DESC''')
    return cursor.fetchall()

iniciarTabla(c)

#esta = estaLaCancion("Clocks","Coldplay","canciones")
#print(estaLaCancion("Upside Down","Jack Johnson"))
#print(masReproducidas())
#insertarCancion("Will you - fgf &%/$#)=#)$=) ? dasdsa ?","queen")
