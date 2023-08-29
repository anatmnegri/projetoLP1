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
        
# CRUD para Livros
def cadastrar_livro():
    titulo = input('Título: ').strip().lower()
    autor = input('Autor: ').strip().lower()
    preco = int(input('Preço: '))
    livros[titulo] = Livro(titulo, autor, preco)

def listar_livros():
    print(f'{"Título".ljust(25)} Autor')
    for livro in livros.values():
        print(f'{livro.titulo.ljust(30)} {livro.autor}')

def atualizar_livro():
        titulo = input('Título: ').strip().lower()
        if titulo in livros:
            print(f'Preço atual: {livros[titulo].preco}')
        try:
            novo_preco = int(input('Novo preço: '))
            livros[titulo].preco = novo_preco
            print('Preço alterado.')
        except ValueError:
            print('Digite um valor válido.')
        else:
            print('Livro não encontrado.')

def deletar_livro():
        titulo = input('Título: ').strip().lower()
        if titulo in livros:
            resposta = input(f'Você tem certeza que deseja remover {titulo}? ')
            if resposta.lower() == 'sim':
                    del livros[titulo]
                    print('Livro removido.')
            else:
                    print('Remoção cancelada.')
        else:
            print('Livro não encontrado.')

# CRUD para Clientes
def cadastrar_cliente():
        nome = input('Nome: ').strip().lower()
        endereco = input('Endereço: ').strip().lower()
        telefone = int(input('Telefone: '))
        clientes[nome] = Cliente(nome, endereco, telefone)

def listar_clientes():
    print(f'{"Cliente".ljust(25)} Endereço')
    for cliente in clientes.values():
        print(f'{cliente.nome.ljust(30)} {cliente.endereco}')


def atualizar_cliente():
        nome = input('Nome: ').strip().lower()
        if nome in clientes:
            print(f'Endereço atual: {clientes[nome].endereco}')
        try:
            novo_endereco = int(input('Novo endereço: '))
            clientes[nome].endereco = novo_endereco
            print('Endereço alterado.')
        except ValueError:
            print('Digite um valor válido.')
        else:
            print('Cliente não encontrado.')

def deletar_cliente():
        nome = input('Nome: ').strip().lower()
        if nome in clientes:
            resposta = input(f'Você tem certeza que deseja remover {nome}? ')
            if resposta.lower() == 'sim':
                    del clientes[nome]
                    print('Cliente removido.')
            else:
                    print('Remoção cancelada.')
        else:
            print('Cliente não encontrado.')

# Registro de Vendas
def registrar_venda():
        vendas.append(Venda)

def listar_vendas(self):
        return self.vendas

def menuInicial():
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print(f'{"MENU INICIAL".rjust(13)}')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('1-Cadastro de Livros')
    print('2-Cadastro de Clientes')
    print('3-Registrar Venda')
    escolha_menuInicial = input("Escolha: ").strip()

    if escolha_menuInicial == '1':
        menuLivros()
    elif escolha_menuInicial == '2':
        menuClientes()
    elif escolha_menuInicial == '3':
        registrar_venda()
    else:
        print('Você não informou um comando disponível.')

def menuLivros():
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print(f'{"MENU LIVROS".rjust(13)}')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('1-Adicionar Livro')
    print('2-Remover Livro')
    print('3-Alterar Preço')
    print('4-Listar Livros')
    escolha_menuInicial = input("Escolha: ").strip()

    if escolha_menuInicial == '1':
        cadastrar_livro()
    elif escolha_menuInicial == '2':
        deletar_livro()
    elif escolha_menuInicial == '3':
        atualizar_livro()
    elif escolha_menuInicial == '4':
        listar_livros()
    else:
        print('Você não informou um comando disponível.')

def menuClientes():
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print(f'{"MENU Clientes".rjust(13)}')
    print('-=-=-=-=-=-=-=-=-=-=-=')
    print('1-Adicionar Cliente')
    print('2-Remover Cliente')
    print('3-Alterar Cliente')
    print('4-Listar Clientes')
    escolha_menuInicial = input("Escolha: ").strip()

    if escolha_menuInicial == '1':
        cadastrar_cliente()
    elif escolha_menuInicial == '2':
        deletar_cliente()
    elif escolha_menuInicial == '3':
        atualizar_cliente()
    elif escolha_menuInicial == '4':
        listar_clientes()
    else:
        print('Você não informou um comando disponível.')

def main():
    while True:
        menuInicial()

if __name__ == "__main__":
    main()
