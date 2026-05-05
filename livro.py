from item_biblioteca import ItemBiblioteca

class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, autor, num_paginas, disponivel=True):
        super().__init__(codigo, titulo, ano, disponivel)
        self.set_autor(autor)
        self.set_num_paginas(num_paginas)

    def exibir_detalhes(self):
        print(f"Livro - Codigo: {self.get_codigo()} - Titulo: {self.get_titulo()} - Autor: {self.get_autor()} - Paginas: {self.get_num_paginas()} - Ano: {self.get_ano()} - Disponivel: {self.is_disponivel()}")

    def get_autor(self):
        return self.__autor

    def set_autor(self, autor):
        if autor != "":
            self.__autor = autor.strip()
        else:
            raise ValueError("Autor não pode ser vazio.")

    def get_num_paginas(self):
        return self.__num_paginas

    def set_num_paginas(self, num_paginas):
        if num_paginas > 0:
            self.__num_paginas = num_paginas
        else:
            raise ValueError("Número de páginas deve ser inteiro maior que zero.")