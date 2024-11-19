from meuProjeto.app import *
import pytest

# Fixture para criar um estoque vazio
@pytest.fixture
def estoqueVazio():
    return Estoque()

############## TESTES DE UNIDADE DAS CLASSES ###################

# Testes para a classe Produto

# ESSE TESTE VERIFICA A CRIAÇÃO DE UM NOVO PRODUTO
@pytest.mark.classeProduto
def test_criacaoProduto():
    produto = Produto("Mouse", 10)
    assert produto.getNome() == "Mouse"
    assert produto.getQuantidade() == 10

# AQUI TESTA-SE UMA QUANTIDADE VÁLIDA DE PRODUTO
@pytest.mark.classeProduto
def test_quantidadeValida():
    produto = Produto("Teclado", 5)
    produto.setQuantidade(15)
    assert produto.getQuantidade() == 15

# AQUI TESTA-SE UMA QUANTIDADE INVÁLIDA, NESSE CASO NEGATIVA
# E O RETORNO DE UMA EXCEÇÃO PERSONALIZADA
@pytest.mark.classeProduto
def test_SetQuantidadeInvalida():
    produto = Produto("Monitor", 3)
    with pytest.raises(ValueError):
        produto.setQuantidade(-5)

# Testes para a classe Estoque

# TESTE PARA ADICIONAR UM NOVO PRODUTO E SUA QUANTIDADE
@pytest.mark.classeEstoque
def test_adicionarNovoProduto(estoqueVazio):
    produto = Produto("Mouse", 10)
    estoqueVazio.adicionarProdutos(produto)
    assert estoqueVazio.verificaQuantidade("Mouse") == 10

# TESTE PARA ADICIONAR MAIS QUANTIDADE A UM PRODUTO EXISTENTE
@pytest.mark.classeEstoque
def test_adicionarProdutoExistente(estoqueVazio):
    produto1 = Produto("Mouse", 10)
    produto2 = Produto("Mouse", 5)
    estoqueVazio.adicionarProdutos(produto1)
    estoqueVazio.adicionarProdutos(produto2)
    assert estoqueVazio.verificaQuantidade("Mouse") == 15

# TESTE PARA VERIFICAR A CHAMADA DE ALGO INEXISTENTE
@pytest.mark.classeEstoque
def test_produtoInexistente(estoqueVazio):
    with pytest.raises(KeyError):
        estoqueVazio.verificaQuantidade("Teclado")

# TESTE PARA LISTAR OS PRODUTOS EM ESTOQUE
@pytest.mark.classeEstoque
def test_listar_produtos(estoqueVazio):
    produto1 = Produto("Mouse", 10)
    produto2 = Produto("Teclado", 15)
    estoqueVazio.adicionarProdutos(produto1)
    estoqueVazio.adicionarProdutos(produto2)
    assert estoqueVazio.listarProdutos() == ["Mouse: 10", "Teclado: 15"]

########## TESTE de INTEGRAÇÃO #######################

@pytest.mark.appIntegrado
def test_fluxoCompleto(estoqueVazio):
    # Adicionar produtos
    produto1 = Produto("Mouse", 10)
    produto2 = Produto("Teclado", 15)
    estoqueVazio.adicionarProdutos(produto1)
    estoqueVazio.adicionarProdutos(produto2)

    # Verificar adições
    assert estoqueVazio.verificaQuantidade("Mouse") == 10
    assert estoqueVazio.verificaQuantidade("Teclado") == 15

    # Adicionar mais unidades ao estoque
    estoqueVazio.adicionarProdutos(Produto("Mouse", 5))
    assert estoqueVazio.verificaQuantidade("Mouse") == 15

    # Listar produtos
    produtos_listados = estoqueVazio.listarProdutos()
    assert produtos_listados == ["Mouse: 15", "Teclado: 15"]

    # Verificar comportamento com produto inexistente
    with pytest.raises(KeyError):
        estoqueVazio.verificaQuantidade("Monitor")
