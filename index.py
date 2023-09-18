import tkinter as tk
from tkinter import messagebox
import pickle

class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco

class Cliente:
    def __init__(self, nome, endereco, telefone):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone

class Venda:
    def __init__(self, cliente, livros, data, valor_total):
        self.cliente = cliente
        self.livros = livros
        self.data = data
        self.valor_total = valor_total


livros = {}
clientes = {}
vendas = []

class InterfaceGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gerenciamento")

        self.carregar_dados()
        self.menu_inicial()

    def salvar_dados(self):
        with open("dados.pkl", "wb") as arquivo:
            pickle.dump((livros, clientes, vendas), arquivo)

    def carregar_dados(self):
        try:
            with open("dados.pkl", "rb") as arquivo:
                global livros, clientes, vendas
                livros, clientes, vendas = pickle.load(arquivo)
        except FileNotFoundError:
            pass

    def criar_pagina(self, titulo, campos, funcao, voltar_para):
        self.clear_frame()
        self.root.geometry("400x400")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text=titulo, font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        entry_widgets = []
        for campo in campos:
            label = tk.Label(self.root, text=f"{campo}:", bg="#ffffff")
            label.pack(pady=5)
            entry = tk.Entry(self.root, font=("Helvetica", 12))
            entry.pack(pady=5)
            entry_widgets.append(entry)

        button_adicionar = tk.Button(self.root, text=titulo, command=lambda: funcao(entry_widgets), font=("Helvetica", 12))
        button_adicionar.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=voltar_para, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def menu_inicial(self):
        self.clear_frame()
        self.root.geometry("400x300")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="MENU INICIAL", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        button_livros = tk.Button(self.root, text="Cadastro de Livros", command=self.menu_livro, font=("Helvetica", 12))
        button_livros.pack(pady=10)

        button_clientes = tk.Button(self.root, text="Cadastro de Clientes", command=self.menu_clientes, font=("Helvetica", 12))
        button_clientes.pack(pady=10)

        button_vendas = tk.Button(self.root, text="Registrar Venda", command=self.tela_registrar_venda, font=("Helvetica", 12))
        button_vendas.pack(pady=10)

        button_vendas_registradas = tk.Button(self.root, text="Vendas Registradas", command=self.listar_vendas_registradas, font=("Helvetica", 12))
        button_vendas_registradas.pack(pady=10)
        
    def listar_vendas_registradas(self):
        vendas_window = tk.Toplevel(self.root)
        vendas_window.title("Vendas Registradas")

        vendas_listbox = tk.Listbox(vendas_window, font=("Helvetica", 12), selectmode=tk.SINGLE)
        vendas_listbox.pack(pady=20, padx=20)

        # Adicione as vendas à lista
        for i, venda in enumerate(vendas):
            venda_info = f"Venda {i + 1}: Cliente - {venda.cliente.nome}, Data - {venda.data}, Valor Total - R${venda.valor_total:.2f}"
            vendas_listbox.insert(tk.END, venda_info)
            
    def menu_livro(self):
        self.clear_frame()
        self.root.geometry("400x350")

        label = tk.Label(self.root, text="MENU LIVROS", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        button_adicionar = tk.Button(self.root, text="Adicionar Livro", command=self.tela_cadastrar_livros, font=("Helvetica", 12))
        button_adicionar.pack(pady=10)

        button_remover = tk.Button(self.root, text="Remover Livro", command=self.deletar_livro, font=("Helvetica", 12))
        button_remover.pack(pady=10)

        button_alterar = tk.Button(self.root, text="Alterar Preço", command=self.atualizar_livro, font=("Helvetica", 12))
        button_alterar.pack(pady=10)

        button_listar = tk.Button(self.root, text="Listar Livros", command=self.listar_livros, font=("Helvetica", 12))
        button_listar.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_inicial, font=("Helvetica", 12))
        button_voltar.pack(pady=10)
    
    def menu_clientes(self):
        self.clear_frame()
        self.root.geometry("400x350")

        label = tk.Label(self.root, text="MENU CLIENTES", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        button_adicionar = tk.Button(self.root, text="Adicionar Cliente", command=self.tela_cadastrar_cliente, font=("Helvetica", 12))
        button_adicionar.pack(pady=10)

        button_remover = tk.Button(self.root, text="Remover Cliente", command=self.deletar_cliente, font=("Helvetica", 12))
        button_remover.pack(pady=10)

        button_alterar = tk.Button(self.root, text="Alterar Cliente", command=self.atualizar_cliente, font=("Helvetica", 12))
        button_alterar.pack(pady=10)

        button_listar = tk.Button(self.root, text="Listar Clientes", command=self.listar_clientes, font=("Helvetica", 12))
        button_listar.pack(pady=10) 

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_inicial, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def tela_cadastrar_livros(self):
        campos = ["Título", "Autor", "Preço"]
        self.criar_pagina("CADASTRAR LIVRO", campos, self.cadastrar_livro, self.menu_livro)
        

    def tela_cadastrar_cliente(self):
        campos = ["Nome", "Endereço", "Telefone"]
        self.criar_pagina("CADASTRAR CLIENTE", campos, self.cadastrar_cliente, self.menu_clientes)

    def tela_registrar_venda(self):
        campos = ["Nome do Cliente", "Livros (separados por vírgula)", "Data da Venda"]
        self.criar_pagina("REGISTRAR VENDA", campos, self.registrar_venda_final, self.menu_inicial)

    def cadastrar_livro(self, entry_widgets):
        valores = [entry.get().strip().lower() for entry in entry_widgets]
        titulo, autor, preco = valores
        livros[titulo] = Livro(titulo, autor, float(preco))
        self.salvar_dados()

    def deletar_livro(self):
        self.clear_frame()
        self.root.geometry("400x250")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="REMOVER LIVRO", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        label_titulo = tk.Label(self.root, text="Título do livro a ser removido:", bg="#ffffff")
        label_titulo.pack(pady=5)
        self.entry_titulo = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_titulo.pack(pady=5)

        button_remover = tk.Button(self.root, text="Remover Livro", command=self.remover_livro, font=("Helvetica", 12))
        button_remover.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_livro, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def remover_livro(self):
        titulo = self.entry_titulo.get().strip().lower()
        if titulo in livros:
            del livros[titulo]
            self.salvar_dados()
            messagebox.showinfo("Livro Removido", f"Livro '{titulo}' removido com sucesso!")
        else:
            messagebox.showerror("Erro", f"Livro '{titulo}' não encontrado")

    def atualizar_livro(self):
        self.clear_frame()
        self.root.geometry("400x320")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="ATUALIZAR PREÇO DO LIVRO", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        label_titulo = tk.Label(self.root, text="Título do livro a ser atualizado:", bg="#ffffff")
        label_titulo.pack(pady=5)
        self.entry_titulo = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_titulo.pack(pady=5)

        label_preco = tk.Label(self.root, text="Novo preço:", bg="#ffffff")
        label_preco.pack(pady=5)
        self.entry_preco = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_preco.pack(pady=5)

        button_atualizar = tk.Button(self.root, text="Atualizar Preço", command=self.atualizar_preco_livro, font=("Helvetica", 12))
        button_atualizar.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_livro, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def atualizar_preco_livro(self):
        titulo = self.entry_titulo.get().strip().lower()
        if titulo in livros:
            novo_preco = float(self.entry_preco.get())
            livros[titulo].preco = novo_preco
            self.salvar_dados()
            messagebox.showinfo("Preço Atualizado", f"Preço do livro '{titulo}' atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", f"Livro '{titulo}' não encontrado")

    def listar_livros(self):
        lista = "\n".join([f"{livro.titulo} - {livro.autor} - R${livro.preco:.2f}" for livro in livros.values()])
        messagebox.showinfo("Livros Cadastrados", lista)

    def cadastrar_cliente(self, entry_widgets):
        valores = [entry.get().strip().lower() for entry in entry_widgets]
        nome, endereco, telefone = valores
        clientes[nome] = Cliente(nome, endereco, telefone)
        self.salvar_dados()

    def deletar_cliente(self):
        self.clear_frame()
        self.root.geometry("400x250")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="REMOVER CLIENTE", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        label_nome = tk.Label(self.root, text="Nome do cliente a ser removido:", bg="#ffffff")
        label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_nome.pack(pady=5)

        button_remover = tk.Button(self.root, text="Remover Cliente", command=self.remover_cliente, font=("Helvetica", 12))
        button_remover.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_clientes, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def remover_cliente(self):
        nome = self.entry_nome.get().strip().lower()
        if nome in clientes:
            del clientes[nome]
            self.salvar_dados()
            messagebox.showinfo("Cliente Removido", f"Cliente '{nome}' removido com sucesso!")
        else:
            messagebox.showerror("Erro", f"Cliente '{nome}' não encontrado")


    def atualizar_cliente(self):
        self.clear_frame()
        self.root.geometry("400x320")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="ATUALIZAR ENDEREÇO DO CLIENTE", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        label_nome = tk.Label(self.root, text="Nome do cliente a ser atualizado:", bg="#ffffff")
        label_nome.pack(pady=5)
        self.entry_nome = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_nome.pack(pady=5)

        label_endereco = tk.Label(self.root, text="Novo endereço:", bg="#ffffff")
        label_endereco.pack(pady=5)
        self.entry_endereco = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_endereco.pack(pady=5)

        button_atualizar = tk.Button(self.root, text="Atualizar Endereço", command=self.atualizar_endereco_cliente, font=("Helvetica", 12))
        button_atualizar.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_inicial, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def atualizar_endereco_cliente(self):
        nome = self.entry_nome.get().strip().lower()
        if nome in clientes:
            novo_endereco = self.entry_endereco.get().strip().lower()
            clientes[nome].endereco = novo_endereco
            self.salvar_dados()
            messagebox.showinfo("Endereço Atualizado", f"Endereço do cliente '{nome}' atualizado com sucesso!")
        else:
            messagebox.showerror("Erro", f"Cliente '{nome}' não encontrado")

    def listar_clientes(self):
        lista = "\n".join([f"{cliente.nome} - {cliente.endereco} - {cliente.telefone}" for cliente in clientes.values()])
        messagebox.showinfo("Clientes Cadastrados", lista)

    def registrar_venda(self):
        self.clear_frame()
        self.root.geometry("400x400")
        self.root.configure(bg="#ffffff")

        label = tk.Label(self.root, text="REGISTRAR VENDA", font=("Helvetica", 16), bg="#ffffff")
        label.pack(pady=20)

        label_cliente = tk.Label(self.root, text="Nome do Cliente:", bg="#ffffff")
        label_cliente.pack(pady=5)
        self.entry_cliente = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_cliente.pack(pady=5)

        label_livros = tk.Label(self.root, text="Livros (separados por vírgula):", bg="#ffffff")
        label_livros.pack(pady=5)
        self.entry_livros = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_livros.pack(pady=5)

        label_data = tk.Label(self.root, text="Data da Venda:", bg="#ffffff")
        label_data.pack(pady=5)
        self.entry_data = tk.Entry(self.root, font=("Helvetica", 12))
        self.entry_data.pack(pady=5)

        button_registrar = tk.Button(self.root, text="Registrar Venda", command=self.registrar_venda_final, font=("Helvetica", 12))
        button_registrar.pack(pady=10)

        button_voltar = tk.Button(self.root, text="Voltar", command=self.menu_inicial, font=("Helvetica", 12))
        button_voltar.pack(pady=10)

    def registrar_venda_final(self):
        cliente_nome = self.entry_cliente.get().strip().lower()
        if cliente_nome in clientes:
            livros_venda = self.entry_livros.get().strip().lower().split(',')
            valor_total = 0
            for livro_titulo in livros_venda:
                if livro_titulo in livros:
                    valor_total += livros[livro_titulo].preco
                else:
                    messagebox.showerror("Erro", f"Livro '{livro_titulo}' não encontrado")
                    return
            
            data = self.entry_data.get().strip()
            venda = Venda(clientes[cliente_nome], livros_venda, data, valor_total)
            vendas.append(venda)
            messagebox.showinfo("Venda Registrada", "Venda registrada com sucesso!")
        else:
            messagebox.showerror("Erro", f"Cliente '{cliente_nome}' não encontrado")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = InterfaceGrafica(root)
    root.mainloop()

if __name__ == "__main__":
    main()
