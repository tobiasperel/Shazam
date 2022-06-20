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

def migrarTabla(tabla):
    cursor = c
    cursor = cursor.execute(f"SELECT * from {tabla}")
    #print(cursor.fetchall())
    for row in cursor.fetchall():
        print(row)
        if estaLaCancion(row[1],row[2]):
            continue
        insertarCancion(row[1],row[2])

def insertarCancion(cancion,artista,cantidadDeVecesRepoducida = 1):
    c.execute(f'''INSERT INTO cancionesConReproducciones (
            cancion,artista,cantidadDeVecesRepoducida)VALUES("{cancion}","{artista}","{cantidadDeVecesRepoducida}")''')
    conn.commit()

def pasarTablaADiccionario(tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f"SELECT * from {tabla}")
    diccionario = {}
    for row in cursor:
        diccionario[row[2]] = list()
        for i in range(len(row)):
            print(row[i])
            if i == 0 :
                continue
            if i == 2:
                continue
            if i == 3:
                continue
            diccionario[row[2]].append(row[1])
            diccionario[row[2]].append(row[3])
            continue
    return(diccionario)

def estaLaCancion(cancion, artista, tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f"SELECT * from {tabla} WHERE cancion = '?' AND artista = '?'".format(cancion,artista))
    if len(cursor.fetchall()) == 0:
        return False
    return True

def agregarReproducciones(cancion,artista, tabla = "cancionesConReproducciones"):
    cursor = c
    cursor = cursor.execute(f"SELECT * from {tabla} WHERE cancion = '?' AND artista = '?'".format(cancion,artista))
    cantidadDeVecesRepoducida = cursor.fetchall()
    print(cantidadDeVecesRepoducida)
    #cursor = cursor.execute("UPDATE cancionesConReproducciones SET cantidadDeVecesRepoducida = {cantidadDeVecesRepoducida} + 1 where cancion = '{cancion}' AND artista = '{artista}'".format(cantidadDeVecesRepoducida = cantidadDeVecesRepoducida,cancion = cancion,artista = artista))
    #conn.commit()


'''
cursor = c
cursor = cursor.execute(f"DROP TABLE cancionesConReproducciones")
''' 
iniciarTabla(c)
#migrarTabla("canciones")
#esta = estaLaCancion("Clocks","Coldplay","canciones")
print(estaLaCancion("Sometimes","Erasure"))
#diccionario = pasarTablaADiccionario()
#print(diccionario)
#insertarCancion("Will you - fgf &%/$#)=#)$=) ? dasdsa ?","queen")
