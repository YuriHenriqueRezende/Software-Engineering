class Produto:
    def __init__(self, nome, quantidade):
        self.__nome = nome  # encapsulamento privado
        self.__quantidade = quantidade

    def getNome(self):
        return self.__nome

    def getQuantidade(self):
        return self.__quantidade

    def setQuantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            raise ValueError("Quantidade não pode ser negativa.")


class Estoque:
    def __init__(self):
        # Usar um dicionário para armazenar produtos, onde as chaves são os nomes dos produtos
        self.__produtos = {}

    def adicionarProdutos(self, produto):
        if not isinstance(produto, Produto):
            raise TypeError("Somente instâncias da classe Produto podem ser adicionadas ao estoque.")
        nome = produto.getNome()
        quantidade = produto.getQuantidade()
        if nome in self.__produtos:  # Atualizar quantidade do produto já existente
            self.__produtos[nome].setQuantidade(
                self.__produtos[nome].getQuantidade() + quantidade
            )
        else:  # Adicionar novo produto ao estoque
            self.__produtos[nome] = produto

    def verificaQuantidade(self, nomeProduto):
        produto = self.__produtos.get(nomeProduto)
        if produto:
            return produto.getQuantidade()
        else:
            raise KeyError(f"Produto '{nomeProduto}' não encontrado no estoque.")

    def listarProdutos(self):
        return [f"{produto.getNome()}: {produto.getQuantidade()}" for produto in self.__produtos.values()]


############ TESTE DA APLICAÇÃO #######################

# Criando produtos
produto1 = Produto("Mouse", 10)
produto2 = Produto("Teclado", 15)

# Criando o estoque
estoque = Estoque()

# Adicionando produtos ao estoque
estoque.adicionarProdutos(produto1)
estoque.adicionarProdutos(produto2)

# Verificando quantidade de produtos no estoque
print("Quantidade de Mouse:", estoque.verificaQuantidade("Mouse"))
print("Quantidade de Teclado:", estoque.verificaQuantidade("Teclado"))

# Adicionando mais unidades ao estoque
estoque.adicionarProdutos(Produto("Mouse", 5))
print("Quantidade de Mouse após adição:", estoque.verificaQuantidade("Mouse"))

# Listando todos os produtos no estoque
print("Produtos no estoque:")
print("\n".join(estoque.listarProdutos()))
