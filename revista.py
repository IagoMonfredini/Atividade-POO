from item_biblioteca import ItemBiblioteca

class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, ano, edicao, mes, disponivel=True):
        super().__init__(codigo, titulo, ano, disponivel)
        self.set_edicao(edicao)
        self.set_mes(mes)

    def exibir_detalhes(self):
        print(f"Revista - Codigo: {self.get_codigo()} - Titulo: {self.get_titulo()} - Edicao: {self.get_edicao()} - Mes: {self.get_mes()} - Ano: {self.get_ano()} - Disponivel: {self.is_disponivel()}")

    def get_edicao(self):
        return self.__edicao

    def set_edicao(self, edicao):
        if edicao > 0:
            self.__edicao = edicao
        else:
            raise ValueError("Edição deve ser inteiro maior que zero.")

    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        if mes.strip() != "":
            self.__mes = mes.strip()
        else:
            raise ValueError("Mês não pode ser vazio.")
