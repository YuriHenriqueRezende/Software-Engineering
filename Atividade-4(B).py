
# Classe ItemBiblioteca
class ItemBiblioteca:
    def __init__(self, codigo, titulo):
        self.__codigo = codigo
        self.__titulo = titulo

    def getCodigoBiblioteca(self):
        return self.__codigo

    def getTitulo(self):
        return self.__titulo


# Classe Livro (herda de ItemBiblioteca)
class Livro(ItemBiblioteca):
    def __init__(self, codigo, titulo, autor, genero):
        super().__init__(codigo, titulo)
        self.__autor = autor
        self.__genero = genero

    def getAutor(self):
        return self.__autor

    def getGenero(self):
        return self.__genero


# Classe Revista (herda de ItemBiblioteca)
class Revista(ItemBiblioteca):
    def __init__(self, codigo, titulo, edicao, mes_publicacao):
        super().__init__(codigo, titulo)
        self.__edicao = edicao
        self.__mes_publicacao = mes_publicacao

    def getEdicao(self):
        return self.__edicao

    def getPublicacao(self):
        return self.__mes_publicacao


# Classe Biblioteca
class Biblioteca:
    def __init__(self, nome):
        self.__nome = nome
        self.__itens_biblioteca = []

    def getNome(self):
        return self.__nome

    def getItensBiblioteca(self):
        return self.__itens_biblioteca

    def addItem(self, item):
        self.__itens_biblioteca.append(item)

    def remItem(self, codigo):
        self.__itens_biblioteca = [
            item for item in self.__itens_biblioteca if item.getCodigoBiblioteca() != codigo
        ]

if __name__ == "__main__":
    # Criando itens de biblioteca
    livro1 = Livro(1, "O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
    revista1 = Revista(2, "Revista de Tecnologia", 15, "2023-09-01")

    # Criando uma biblioteca e adicionando itens
    biblioteca = Biblioteca("Biblioteca do Yuri e Vitor")
    biblioteca.addItem(livro1)
    biblioteca.addItem(revista1)

    # Exibindo itens da biblioteca
    print(f"Biblioteca: {biblioteca.getNome()}")
    for item in biblioteca.getItensBiblioteca():
        print(f"Item: {item.getTitulo()}, Código: {item.getCodigoBiblioteca()}")

    # Removendo um item da biblioteca
    biblioteca.remItem(1)

    # Exibindo itens após remoção
    print("\nApós remoção:")
    for item in biblioteca.getItensBiblioteca():
        print(f"Item: {item.getTitulo()}, Código: {item.getCodigoBiblioteca()}")
