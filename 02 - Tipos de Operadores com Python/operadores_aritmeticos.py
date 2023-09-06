# Os Operadores Aritméticos executam operações matemáticas, como adição, subtração com operandos.
produto1 = 20
produto2 = 10

print("Soma = ", produto1 + produto2)
print("Subtracao = ", produto1 - produto2)
print("Divisao = ", produto1 / produto2)
print("Divisao inteira = ", produto1 // produto2)
print("Multiplicacao = ", produto1 * produto2)
print("Modulo (resto da divisão) = ", produto1 % produto2)
print("Exponenciacao = ", produto1 ** produto2)

# Em Python a ordem de execução das operações são: Parênteses, Expoêntes
# Multiplicações e divisões (da esquerda para a direita)
# Somas e subtrações (da esquerda para a direita)
operacao = 10 + 5 * 4

print(f"Resultado = {operacao}")

print(10 - 5 * 2)
print((10 - 5) * 2)
