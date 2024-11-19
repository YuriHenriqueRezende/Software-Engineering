import pytest

########## FUNÇÕES BÁSICAS ##########################
def emailValido(email):
    return "@" in email and "." in email

# def dividir(a, b):
#     if b == 0:
#         raise ZeroDivisionError
#     return a / b

def dividir(a, b):
    # if b == 0:
    #     return None
    return a / b

######################################################

######### ESTRUTURAS DE DADOS ########################

def calcularMedia(numeros):
    """
    Calcula a média de uma lista de números.
    
    Args:
        numeros: Uma lista de números.
        
    Returns:
        A média dos números na lista.
    """
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    return soma / len(numeros)

#####################################################

def calcularTotal(preco, valorDesconto, taxaImposto):
    if valorDesconto > 0.2:
        valorDesconto = 0.2
    elif valorDesconto < 0 or valorDesconto is None:
        valorDesconto = 0
    if taxaImposto < 0 or taxaImposto is None:
        taxaImposto = 0
    desconto = preco * valorDesconto
    imposto = (preco - desconto) * taxaImposto
    total = preco - (desconto + imposto)
    return round(total, 2)

###########################################################

def verificaIdade(idade):
    if idade < 18:
        raise ValueError("Acesso negado para menores de 18 anos!")
    return ("Acesso permitido!")
