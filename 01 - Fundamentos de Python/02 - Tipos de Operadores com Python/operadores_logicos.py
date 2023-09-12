# Os Operadores Lógicos são utilizados em conjunto com os operadores de comparação, 
# para montar uma expressão lógica. Quando utilizado o resultado retornado é um booleano.
# and = para ser True tudo tem que ser True.
# or = para ser True apenas um tem que ser true.
saldo = 1000
saque = 250
limite = 200
conta_especial = True

expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

# É recomendado usarmos parenteses para dar mais legibilidade e separar o código
expressao_1 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_1)

saldo_suficiente = (saldo >= saque and saque <= limite)

conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)
expressao_2 = saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_2)

