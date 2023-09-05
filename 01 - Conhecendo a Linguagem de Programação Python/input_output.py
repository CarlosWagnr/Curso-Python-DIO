# A função input permite inserir um valor de entrada a uma variável.
# A função print exibe uma mensagem de saída 
nome_entrada = input("Informe seu nome: ")
idade_entrada = input("Informe sua idade: ")

print(nome_entrada, idade_entrada)
print(nome_entrada, idade_entrada, end="...\n")
print(nome_entrada, idade_entrada, sep=",")
print(nome_entrada, idade_entrada, sep="#", end="...\n")
