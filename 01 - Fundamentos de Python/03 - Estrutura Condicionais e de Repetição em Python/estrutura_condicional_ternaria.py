# O if ternário permite escrever uma condiçãoem uma única linha.
saldo = 2000
saque = 500
status = "Sucesso" if saque <= saldo else "Falha"

print(f"{status} ao realizar o saque!")