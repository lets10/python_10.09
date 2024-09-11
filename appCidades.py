import tkinter as tk
from Cidades import cidades
import Banco as Banco

class appCidades:
    def __init__(self, master=None):
        self.cidades_db = cidades()
        self.janela1 = tk.Frame(master)
        self.janela1.pack()
        self.msg1 = tk.Label(self.janela1, text="Informe os dados da Cidade:")
        self.msg1["font"] = ("Verdana", 12, "bold")
        self.msg1.pack()

        self.janela2 = tk.Frame(master)
        self.janela2["padx"] = 20
        self.janela2.pack()

        self.idcidades_label = tk.Label(self.janela2, text="Id cidade:")
        self.idcidades_label.pack(side="left")
        self.idcidades = tk.Entry(self.janela2, width=30)
        self.idcidades.pack(side="left")

        self.busca = tk.Button(self.janela2, text="buscar", command=self.buscarcidades)
        self.busca.pack()

        self.janela3 = tk.Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack()

        self.nome_label = tk.Label(self.janela3, text="Cidade:")
        self.nome_label.pack(side="left")
        self.nome = tk.Entry(self.janela3, width=30)
        self.nome.pack(side="left")

        self.janela5 = tk.Frame(master)
        self.janela5["padx"] = 20
        self.janela5.pack(pady=5)

        self.uf_label = tk.Label(self.janela5, text="UF:")
        self.uf_label.pack(side="left")
        self.uf = tk.Entry(self.janela5, width=30)
        self.uf.pack(side="left")

        self.janela10 = tk.Frame(master)
        self.janela10["padx"] = 20
        self.janela10.pack()

        self.autentic = tk.Label(self.janela10, text="")
        self.autentic["font"] = ("Verdana", 10, "italic", "bold")
        self.autentic.pack()

        self.janela11 = tk.Frame(master)
        self.janela11["padx"] = 20
        self.janela11.pack()

        self.botao = tk.Button(self.janela11, width=10, text="inserir", command=self.insertCidade)
        self.botao.pack(side="left")
        self.botao2 = tk.Button(self.janela11, width=10, text="alterar", command=self.updateCidade)
        self.botao2.pack(side="left")
        self.botao3 = tk.Button(self.janela11, width=10, text="excluir", command=self.deleteCidade)
        self.botao3.pack(side="left")

    def buscarcidades(self):
        idcidades = self.idcidades.get()
        self.cidades_db.selectUser(idcidades)
        if self.cidades_db.nome:
            self.autentic["text"] = "Cidade encontrada."
            self.nome.delete(0, tk.END)
            self.nome.insert(tk.INSERT, self.cidades_db.nome)
            self.uf.delete(0, tk.END)
            self.uf.insert(tk.INSERT, self.cidades_db.UF)
        else:
            self.autentic["text"] = "Cidade não encontrada."
            self.limparCampos()

    def insertCidade(self):
        self.cidades_db.nome = self.nome.get()
        self.cidades_db.UF = self.uf.get()
        result = self.cidades_db.insertUser()
        self.autentic["text"] = result
        self.limparCampos()

    def updateCidade(self):
        self.cidades_db.idcidades = self.idcidades.get()
        self.cidades_db.nome = self.nome.get()
        self.cidades_db.UF = self.uf.get()
        result = self.cidades_db.updateUser()
        self.autentic["text"] = result
        self.limparCampos()

    def deleteCidade(self):
        self.cidades_db.idcidades = self.idcidades.get()
        result = self.cidades_db.deleteUser()
        self.autentic["text"] = result
        self.limparCampos()

    def limparCampos(self):
        self.idcidades.delete(0, tk.END)
        self.nome.delete(0, tk.END)
        self.uf.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    appCidades(root)
    root.mainloop()
