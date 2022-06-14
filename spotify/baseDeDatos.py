import sqlite3
try:
    conn = sqlite3.connect('spotify/database.db')
except:
    conn = sqlite3.connect('database.db')
c = conn.cursor()

def iniciarTabla(c):
    c.execute('''CREATE TABLE IF NOT EXISTS "canciones" 
                ("ID"	INTEGER NOT NULL,
                "cancion"	TEXT,
                "artista"	TEXT,
                PRIMARY KEY("ID" AUTOINCREMENT)
                );''')
    conn.commit()

def insertarCancion(cancion,artista):
    c.execute(f'''INSERT INTO canciones (
            cancion,artista)VALUES("{cancion}","{artista}")''')
    conn.commit()

def pasarTablaADiccionario(tabla = "canciones", relevant=1):
    cursor = c
    cursor = cursor.execute(f"SELECT * from {tabla}")
    diccionario = {}
    for row in cursor:
        diccionario[row[2]] = ""
        for i in range(len(row)):
            if i == 0 :
                continue
            if i == 2:
                continue
            diccionario[row[2]] = row[i]
    return(diccionario)

iniciarTabla(c)

#diccionario = pasarTablaADiccionario()
#print(diccionario)
#insertarCancion("one","queen")
