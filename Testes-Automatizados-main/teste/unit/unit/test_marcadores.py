import pytest
import sys

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
@pytest.mark.slow  # Exemplo de marcador adicional
def test_ui_login():
    # Simulação de um teste de interface do usuário
    assert True
