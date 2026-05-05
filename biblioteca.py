class Biblioteca:
    def __init__(self):
        self.__itens = []

    def adicionar_item(self, item):
        # aceita instâncias de Livro ou Revista (ou subclasses de ItemBiblioteca)
        self.__itens.append(item)
        print(f"Item adicionado: {item.get_codigo()} - {item.get_titulo()}")

    def listar_itens(self):
        if not self.__itens:
            print("Nenhum item cadastrado.")
            return
        for item in self.__itens:
            item.exibir_detalhes()

    def buscar_por_codigo(self, codigo):
        for item in self.__itens:
            if item.get_codigo() == codigo:
                return item
        return None

    def emprestar_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.emprestar()
        else:
            print(f"Nenhum item encontrado com código {codigo}.")

    def devolver_item(self, codigo):
        item = self.buscar_por_codigo(codigo)
        if item:
            item.devolver()
        else:
            print(f"Nenhum item encontrado com código {codigo}.")