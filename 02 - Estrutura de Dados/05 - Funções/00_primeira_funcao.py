# Função é um bloco de código identificado por um nome e pode receber uma lista de parâmetros.
def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2("Wagner")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
