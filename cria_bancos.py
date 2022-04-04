import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS Hoteis(Hotel_id text PRIMARY KEY,\
               Nome text,Estrelas real,Diaria real,Cidade text)"

cria_hotel = "INSERT INTO Hoteis VALUES ('01','Hotellum',3.4,154.75,'São Luis')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)
connection.commit()
connection.close()
