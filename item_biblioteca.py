class ItemBiblioteca:
    def __init__(self, codigo, titulo, ano, disponivel):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.__disponivel = disponivel

    def exibir_detalhes(self):
        print(f"Titulo: {self.titulo} - Ano: {self.ano} - Disponivel: {self.disponivel}")

    def emprestar(self):
        if self.__disponivel == True:
            print(f"O livro {self.titulo} está disponivel ✔")
        else:
            print(f"O livro {self.titulo} não está disponivel ✖")

    def devolver(self):
        if self.__disponivel == False:
            print(f"Livro {self.titulo} foi devolvido com sucesso ✔")
        else:
            print(f"Não foi possivel devolver o livro {self.titulo} no momento ✖")