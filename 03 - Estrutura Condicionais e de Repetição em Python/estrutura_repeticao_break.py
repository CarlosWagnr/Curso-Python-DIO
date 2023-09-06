# O comando 'break' para a execução de acordo com condição proposta no código.
# Exemplo com While.
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)


# Exemplo com For.
print()
for num in range(30):
    if num == 10:
        break

    print(num, end=" ")

# O comando 'continue' quando quisermos pular uma determinada execução do código
# Exemplo do For com continue.
print()
for num in range(30):
    if num == 12:
        continue

    print(num, end=" ")
