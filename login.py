import tkinter as tk
from tkinter import messagebox
from tkinter import *
from Banco import Banco

class TeladeLogin:
    def __init__(self, master=None):
        self.master = master
        self.master.title("Tela de Login")
        self.fonte = ("Times New Roman", "10")

        self.janela = Frame(master)
        self.janela["padx"] = 20
        self.janela["pady"] = 5
        self.janela.pack()
        self.img = PhotoImage(file="images.png")
        self.lblimg = Label(self.janela, image=self.img)
        self.lblimg.pack()

        self.container = tk.Frame(master)
        self.container["padx"] = 20
        self.container["pady"] = 20
        self.container.pack()

        self.lblusuario = tk.Label(self.container, text="Usuário:", font=self.fonte)
        self.lblusuario.pack(pady=5)

        self.usuario = tk.Entry(self.container, font=self.fonte)
        self.usuario.pack(pady=5)

        self.lblsenha = tk.Label(self.container, text="Senha:", font=self.fonte)
        self.lblsenha.pack(pady=5)

        self.senha = tk.Entry(self.container, show="*", font=self.fonte)
        self.senha.pack(pady=5)

        self.btnlogin = tk.Button(self.container, text="Entrar", font=self.fonte, command=self.login)
        self.btnlogin.pack(pady=10)

    def login(self):
        usuario = self.usuario.get()
        senha = self.senha.get()

        if self.validar_login(usuario, senha):
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")

        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    def validar_login(self, usuario, senha):

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (usuario, senha))
            linha = c.fetchone()
            c.close()
            return linha is not None
        except Exception as e:
            print(f"Erro ao validar login: {e}")
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = TeladeLogin(root)
    root.mainloop()
