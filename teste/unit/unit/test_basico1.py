from meuProjeto.funcoes import *
import pytest
from meuProjeto.funcoes import dividir

@pytest.mark.funcoes
def test_emailValido():
    assert emailValido("exemplo@dominio.com") is True
    assert emailValido("exemplo.com") is False

import pytest
from meuProjeto.funcoes import dividir  

@pytest.mark.funcoes
def test_dividir1():
    assert dividir(4, 2) == 2
    # assert dividir(4, 0) is None 


@pytest.mark.funcoes
def test_calcular_media_lista_vazia():
    assert calcularMedia([]) == 0

@pytest.mark.funcoes
def test_calcular_media_lista_com_um_elemento():
    assert calcularMedia([5]) == 5

@pytest.mark.funcoes
def test_calcular_media_lista_com_multiplos_elementos():
    assert calcularMedia([1, 2, 3, 4, 5]) == 3

@pytest.mark.funcoes
def test_calcular_media_lista_com_elementos_negativos():
    assert calcularMedia([-1, -2, -3]) == -2
