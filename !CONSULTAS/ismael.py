import sqlite3
import pandas as pd
import json


class DataBase():
    def __init__(self, name = 'system.db') -> None:
        self.name = name

    def connect(self):
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except:
            pass
    
    def criar_tabela(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Pessoas(
                NOME TEXT,
                IDADE TEXT,

                PRIMARY KEY(NOME)
            );
        ''')

    def registar_pessoa(self, dados):

        campos_tabela = ('NOME', 'IDADE')
        qntd = ('?,?')

        cursor = self.connection.cursor()
        
        try:
            cursor.execute(f'''
                INSERT INTO Pessoas {campos_tabela}
                VALUES({qntd})''', dados)

            self.connection.commit()
            return 'ok'
        except:
            return 'Erro'

    def ver_pessoas(self):
        cursor = self.connection.cursor()
        cursor.execute('''SELECT * FROM Pessoas''')
        pessoas = cursor.fetchall()
        return pessoas


if __name__ == '__main__':
    db = DataBase()
    db.connect()
    db.criar_tabela()

    db.close_connection()



db = DataBase()
db.connect()

pessoas = db.ver_pessoas()

pessoas = json.dumps(pessoas)


df = pd.read_json(pessoas)
print(df)

db.close_connection()

