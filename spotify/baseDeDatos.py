import sqlite3
conn = sqlite3.connect('spotify/database.db')
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

print("Opened database successfully")
iniciarTabla(c)
#insertarCancion("one","queen")
