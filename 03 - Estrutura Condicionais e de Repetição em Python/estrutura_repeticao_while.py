# Estrutura de repetição são utilizadas para um trecho de código para serem executados um determinado número de vezes.
# O comando 'while'é usado para repetir um bloco de código várias vezes, faz sentido usarmos quando não sabemos o número exato de vezes que deve executar.
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

else:
    print("Obrigado por usar nosso sistema bancário, até logo!")
    