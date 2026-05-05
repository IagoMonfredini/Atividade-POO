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

        if opcao == "1":
            codigo = input("Código: ").strip()
            titulo = input("Título: ").strip()
            ano = ler_int("Ano: ")
            autor = input("Autor: ").strip()
            num_paginas = ler_int("Número de páginas: ")
            try:
                livro = Livro(codigo, titulo, ano, autor, num_paginas)
                biblioteca.adicionar_item(livro)
            except Exception as e:
                print(f"Erro ao cadastrar livro: {e}")

        elif opcao == "2":
            codigo = input("Código: ").strip()
            titulo = input("Título: ").strip()
            ano = ler_int("Ano: ")
            edicao = ler_int("Edição (número): ")
            mes = input("Mês: ").strip()
            try:
                revista = Revista(codigo, titulo, ano, edicao, mes)
                biblioteca.adicionar_item(revista)
            except Exception as e:
                print(f"Erro ao cadastrar revista: {e}")

        elif opcao == "3":
            biblioteca.listar_itens()

        elif opcao == "4":
            codigo = input("Digite o código do item a emprestar: ").strip()
            biblioteca.emprestar_item(codigo)

        elif opcao == "5":
            codigo = input("Digite o código do item a devolver: ").strip()
            biblioteca.devolver_item(codigo)

        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()