import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS Hoteis(Hotel_id text PRIMARY KEY,\
               Nome text,Estrelas real,Diaria real,Cidade text)"

cursor.execute(cria_tabela)
connection.commit()
connection.close()
