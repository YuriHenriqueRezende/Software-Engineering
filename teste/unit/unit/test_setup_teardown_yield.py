import pytest

@pytest.fixture
def contador():
    """Fixture que simula um contador."""
    valor = 0  # setup: inicializa o contador
    yield valor  # retorna o valor inicial para o teste
    print("Teardown executado!")  # teardown: executado após o teste

def test_incrementarContador(contador):
    """Incrementa o contador e verifica seu valor."""
    valorInicial = contador
    assert valorInicial == 0  # Verifica o valor inicial
    valorInicial += 1
    assert valorInicial == 1  # Verifica o valor depois do incremento

def test_contadorZero(contador):
    """Verifica se o contador começa em 0."""
    assert contador == 0
