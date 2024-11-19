from meuProjeto.funcoes import *
import pytest
import sys

@pytest.mark.idade
def test_verficaIdadeComErro():
    with pytest.raises(ValueError):
        verificaIdade(17)

@pytest.mark.idade
def test_verificaIdadeSemErro():
    assert verificaIdade(20) == "Acesso permitido!"

@pytest.mark.dividir
def test_verificaDivZero():
    with pytest.raises(ZeroDivisionError):
        dividir(10,0)

# Marcadores para categorizar os testes
@pytest.mark.unit
def test_funcao_1():
    assert 1 + 1 == 2

@pytest.mark.unit
@pytest.mark.funcao2
def test_funcao_2():
  assert 2 * 2 == 4

@pytest.mark.integration
def test_integracao_banco_de_dados():
    # Simulação de um teste de integração com o banco de dados
    assert True

@pytest.mark.ui
@pytest.mark.slow # Exemplo de marcador adicional
def test_ui_login():
    # Simulação de um teste de interface do usuário
    assert True
