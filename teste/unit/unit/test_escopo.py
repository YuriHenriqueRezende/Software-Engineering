import pytest

# Fixture com escopo de função (function) - default
@pytest.fixture
def contadorFuncao():
    contador = 0
    print()
    print(f"Criando contador de função... Valor inicial: {contador}")
    yield contador
    print(f"Destruindo contador de função... Valor final: {contador}")

# Fixture com escopo de módulo (module)
@pytest.fixture(scope="module")
def contadorModulo():
    contador = 0
    print()
    print(f"Criando contador de módulo... Valor inicial: {contador}")
    yield contador
    print(f"Destruindo contador de módulo... Valor final: {contador}")

# Fixture com escopo de sessão (session)
@pytest.fixture(scope="session")
def contadorSessao():
    contador = 0
    print()
    print(f"Criando contador de sessão... Valor inicial: {contador}")
    yield contador
    print(f"Destruindo contador de sessão... Valor final: {contador}")

def test_contadorFuncao(contadorFuncao):
    print()
    print("Executando teste com contador de função...")
    contadorFuncao += 1
    assert contadorFuncao == 1

def test_contadorModulo(contadorFuncao, contadorModulo):
    print()
    print("Executando teste com contador de função...")
    print("Executando teste com contador de módulo...")
    contadorFuncao += 1
    contadorModulo += 1
    assert contadorFuncao == 1
    assert contadorModulo == 1

def test_contadorSessao(contadorFuncao, contadorModulo, contadorSessao):
    print()
    print("Executando teste com contador de função...")
    print("Executando teste com contador de módulo...")
    print("Executando teste com contador de sessão...")
    contadorFuncao += 1
    contadorModulo += 1
    contadorSessao += 1
    assert contadorFuncao == 1
    assert contadorModulo == 1
    assert contadorSessao == 1
