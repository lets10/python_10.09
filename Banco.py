import tkinter
import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
         c = self.conexao.cursor()
         c.execute("""create table if not exists tbl_usuarios(
          idusuario integer primary key autoincrement,
          nome text,
          telefone text,
          email text,
          usuario text,
          senha text)""")
         self.conexao.commit()
         c.close()

    def createTable(self):
        c = self.conexao.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS tbl_cidades(
                   idcidades INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT,
                   UF TEXT)""")
        self.conexao.commit()
        c.close()



