# Estruturas condicionais permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CHN.")

# if/else: Utilizadas para criar uma estrutura condicional com dois desvios.

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
else:
    print("Ainda não pode tirar a CHN.")

# if/elif/else: Utilizadas para criar uma estrutura condicional com Três ou mais desvios.
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CHN.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CHN.")


