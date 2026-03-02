import item_biblioteca

class Livro(item_biblioteca.ItemBiblioteca):
    def __init__(self, titulo, ano, autor, num_paginas):
        super().__init__(titulo, ano)
    self.__autor = autor
    self.__num_paginas = num_paginas

    def exibir_detalhes(self):
        print("Tipo: Livro")
        super().exibir_detalhes()
        print(f"Autor: {self.autor}")
        print(f"Número de paginas: {self.__paginas}")