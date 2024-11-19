from meuProjeto.funcoes import *
import pytest

@pytest.mark.teste1
@pytest.mark.parametrize("a, b, esperado", [
    (2, 2, 1),
    (-2, -2, 1),
    (-2, 2, -1),
    (2, -2, -1),
    # (10, 0, None)
])
def test_dividir2(a, b, esperado):
    assert dividir(a, b) == esperado

@pytest.mark.preco
@pytest.mark.parametrize("preco", [10.00, 50.00, 100.00])
@pytest.mark.parametrize("valorDesconto", [-0.2, 0.2, 0.4])
@pytest.mark.parametrize("taxaImposto", [-0.1, 0, 0.1])
def test_calcularTotal(preco, valorDesconto, taxaImposto):
    if valorDesconto > 0.2:
        valorDesconto = 0.2
    elif valorDesconto < 0 or valorDesconto is None:
        valorDesconto = 0

    if taxaImposto < 0 or taxaImposto is None:
        taxaImposto = 0

    descontoEsperado = preco * valorDesconto
    taxaImpostoEsperado = (preco - descontoEsperado) * taxaImposto
    precoEsperado = preco - (descontoEsperado + taxaImpostoEsperado)

    assert calcularTotal(preco, valorDesconto, taxaImposto) == round(precoEsperado, 2)
