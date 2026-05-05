from biblioteca import Biblioteca
from livro import Livro
from revista import Revista

def ler_int(prompt):
    while True:
        try:
            valor = int(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def main():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Cadastrar Livro")
        print("2. Cadastrar Revista")
        print("3. Listar Itens")
        print("4. Emprestar Item ")
        print("5. Devolver Item")
        print("6. Sair")
        opcao = input("Escolha uma opção: ").strip()

