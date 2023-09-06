# indentação e blocoas de comandos
# Identar código é uma forma de manter o código mais legível, no Python, 
# através do interpretador ele determinar onde um bloco de comando inicia e onde ele termina.

def sacar(valor): # Início do bloco do método
    saldo = 500
    if saldo >= valor: # início do bloco if
        print("Valor sacado!")

    # fim do bloco if
    print("Obrigado por ser nosso cliente!\n")
# fim fo bloco do método


def depositar(valor):
    saldo = 500
    saldo += valor
    return print(f"O seu saldo é de {saldo:.2f}")


sacar(100)

depositar(2000)
