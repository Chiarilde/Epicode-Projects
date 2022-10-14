# CONNESSIONE A DBMS CON CONNETTORE E PANDAS

import mysql.connector

import pandas as pd

from sqlalchemy import create_engine


db_connection_str = "mysql+pymysql://root:nerone87@127.0.0.1/ecommerce"
db_connection = create_engine(db_connection_str)

# Prova con print per avvenuta connessione con Pandas
# pagamento = pd.read_sql("pagamento", db_connection)
# print(pagamento)


conn = mysql.connector.connect(user='root', password='nerone87', host='127.0.0.1', database='ecommerce')


def connection_database(user, password, host, database):
    """
    Funzione per connessione a database
    param user = username
    param password = password
    param host = localhost
    param database = nome database
    return connessione
    """
    try:
        conn = mysql.connector.connect(user=user, password=password, host=host, database=database)
        return conn
    except mysql.connector.errors.DatabaseError as db_error:
        print(db.error.msg)
        sys.exit()


def close_connection(connection):
    connection.close()


# FUNZIONI PER COMPORRE DELLE QUERY DINAMICHE CON CURSOR
# e.g. query1(lista_colonne=['nome', 'cognome'], nome_tabella='utente', lista_ordina=['nome', 'DESC'], condizione='nome LIKE %A', distinct=True)
def query1(lista_colonne, nome_tabella, lista_ordina=None, condizione=None, distinct=False):
    if distinct is False:
        is_distinct = ""
    else:
        is_distinct = "DISTINCT"

    if lista_ordina is None:
        is_ordina = ""
    else:       # lista_ordina=['nome', 'DESC'] => 'nome' 'DESC'
        is_ordina = f"ORDER BY {lista_ordina[0]} {lista_ordina[1]}"

    if condizione is None:
        where = ""
    else:
        where = f"WHERE {condizione}"

    cursor = conn.cursor()
    query_stmt = f'SELECT {is_distinct} {", ".join(lista_colonne)} FROM {nome_tabella} {is_ordina} {where};'  #join collega i nomi delle colonne in un'unica stringa separata da virgole
    print(query_stmt)
    cursor.execute(query_stmt)
    result = cursor.fetchall()
    for i in result:
        print(i)


# e.g. join_tables(lista_colonne11=['citta'], nome_tabella1='indirizzo', lista_colonne2=[], nome_tabella2='utente', attr_comune='cognome', distinct=True)
def join_tables(lista_colonne1, nome_tabella1, nome_tabella2, attr_comune, lista_colonne2=None, condizione=None, distinct=False):
    if distinct:
        is_distinct = 'DISTINCT'
    else:
        is_distinct = ''

    if lista_colonne2 is None:
        colonne2 = ''
    else:
        colonne2 = f', {nome_tabella2}.{", ".join(lista_colonne2)}'

    if condizione is None:
        where = ""
    else:
        where = f"WHERE {condizione}"

    cursor = conn.cursor()
    query_stmt = f'SELECT {is_distinct} {nome_tabella1}.{", ".join(lista_colonne1)}' \
                 f'{colonne2} FROM {nome_tabella1} JOIN ' \
                 f'{nome_tabella2} ON {nome_tabella1}.{attr_comune} = {nome_tabella2}.{attr_comune} {where};'

    cursor.execute(query_stmt)
    result = cursor.fetchall()
    print(query_stmt)
    for i in result:
        print(i)

# FUNZIONE PER FARE IL COUNT CON JOIN SU DUE TABELLE
def query2(nome_colonna, count, nome_tabella1, nome_tabella2, attr_comune, group=None):
    if group is None:
        group_by = ''
    else:
        group_by=f"GROUP BY {nome_tabella1}.{group}"
    cursor = conn.cursor()
    query_stmt = f"SELECT {nome_tabella1}.{nome_colonna}, COUNT({nome_tabella2}.{count}) FROM {nome_tabella1} " \
                 f"JOIN {nome_tabella2} ON {nome_tabella1}.{attr_comune} = {nome_tabella2}.{attr_comune} {group_by}"
    cursor.execute(query_stmt)
    result = cursor.fetchall()
    print(query_stmt)
    for i in result:
        print(i)



# CHIAMATE AI METODI

# 1-Visualizza una lista di nomi e cognomi di tutti i clienti
print("----------QUERY 1----------")
query1(['nome', 'cognome'], 'indirizzo', distinct=True)
print("\n")

# 1-Visualizza una lista di nomi e cognomi di tutti i clienti con Pandas
print("----------QUERY 1 PANDAS----------")
utente = pd.read_sql("utente", db_connection)
print(utente.loc[:, ['nome', 'cognome']])
print("\n")

# 2-Visualizza una lista di cognomi in ordine ascendente
print("----------QUERY 2----------")
query1(['cognome'], 'utente', ['cognome', 'asc'], distinct=True)

# 2-Visualizza una lista di cognomi in ordine ascendente in Pandas
print("\n")
print("----------QUERY 2 PANDAS----------")
utente = pd.read_sql("utente", db_connection)
u = utente.sort_values('cognome', ascending=True)
print(u.loc[:, ['cognome']])
print("\n")

# 3-Visualizza il nome e cognome dei clienti con relativa città e telefono in ordine alfabetico per citta
print("----------QUERY 3----------")
query1(['nome', 'cognome', 'citta', 'telefono'], 'indirizzo', lista_ordina=['citta', 'ASC'])
print("\n")

print("----------QUERY 3 IN PANDAS----------")
indirizzo = pd.read_sql("indirizzo", db_connection)
i = indirizzo.sort_values('citta', ascending = True)
print(i.loc[:, ['nome', 'cognome', 'citta', 'telefono']])
print("\n")

# 4-Visualizza indirizzi mail degli utenti per i quali non c'è stato invio di newsletter
print("----------QUERY 4----------")
query1(['nome', 'cognome', 'email'], 'utente', condizione='newsletter LIKE 0')
print("\n")


# 5-Unisce due tabelle diverse per visualizzare cognome e relativo codice fiscale
print("----------QUERY 5----------")
join_tables(['cognome', 'cfisc'], 'indirizzo', 'utente', 'cognome')
print("\n")

# 6-Unisce due tabelle diverse per visualizzare via, citta, cognome e relativa partita iva
print("----------QUERY 6----------")
join_tables(['cognome','via', 'citta', 'piva'], 'indirizzo', 'utente', 'cognome', condizione='piva NOT LIKE "None"')
print("\n")

# 7-Visualizza quanti ordini sono stati spediti e quanti ancora in elaborazione.
print("----------QUERY 7----------")
query2('nome', 'stid', 'stato', 'ordine', 'stid', 'stid')
print("\n")

# 8 Visualizza il nome del prodotto e relativo prezzo
print("----------QUERY 8----------")
join_tables(['nome'], 'prodotto', 'orpr01', 'pid', lista_colonne2=['prezzo'])
print("\n")

# 9-Visualizza quanti ordini sono stati ritirati in sede, consegnati con corriere o spediti per posta
print("----------QUERY 9----------")
query2(nome_colonna='nome', count='uid', nome_tabella1='utente', nome_tabella2='ordine', attr_comune='uid', group='uid')
print("\n")

# 10-Visualizza quanti prodotti fanno parte di ogni categoria
print("----------QUERY 10----------")
query2(nome_colonna='nome', count='pid', nome_tabella1='categoria', nome_tabella2='prodotto', attr_comune='cid', group='cid')