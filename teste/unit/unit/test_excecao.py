from meuProjeto.funcoes import *
import pytest

@pytest.mark.idade
def test_verificaIdadeComErro():
    with pytest.raises(ValueError):
        verificaIdade(17)

@pytest.mark.idade
def test_verificaIdadeSemErro():
    assert verificaIdade(20) == "Acesso permitido!"

@pytest.mark.dividir
def test_verificaDivZero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
