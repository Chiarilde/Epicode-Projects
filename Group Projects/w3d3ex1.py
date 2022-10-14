import mysql.connector

conn = mysql.connector.connect(user='root', password='nerone87', host='127.0.0.1', database='discografia')


def connection_database(user, password, host, database):
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db.error.msg)
        sys.exit()


def close_connection(connection):
    connection.close()

def inserisci_disco(nro_serie, titolo_album, anno, prezzo):
    cursor = conn.cursor()
    query1 = "INSERT INTO disco (NroSerie, TitoloAlbum, Anno, Prezzo) VALUES (%s, %s, %s, %s)"
    val = (nro_serie, titolo_album, anno, prezzo)
    cursor.execute(query1, val)
    conn.commit()

#inserisci_disco('Paranza', 'Paparapa', 2022, 10)

cursor = conn.cursor()
sql = "select * from canzone"
cursor.execute(sql)
result = cursor.fetchall()
print(result)

cursor = conn.cursor()
query2 = "SELECT * FROM canzone JOIN esecuzione ON canzone.CodiceReg=esecuzione.CodiceReg JOIN autore ON esecuzione.TitoloCanzone=autore.TitoloCanzone WHERE nome LIKE '%I';"
cursor.execute(query2)
result2 = cursor.fetchall()
print(result2)

#query che aggiunge una riga di valori da una table

#cursor = conn.cursor()
#query3 = 'INSERT INTO autore (nome, TitoloCanzone) VALUES (%s, %s)'
#val3 = ('O.Pink', 'Audacity');
#cursor.execute(query3, val3)
#conn.commit()

#query che cancella una riga di valori da una table

cursor = conn.cursor()
query4 = "DELETE FROM autore WHERE nome = 'O.Pink'";
cursor.execute(query4)
conn.commit()

cursor = conn.cursor()
query4 = "DELETE FROM disco WHERE Anno = 2022 ";
cursor.execute(query4)
conn.commit()