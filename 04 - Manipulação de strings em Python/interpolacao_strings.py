# Em Python temos 3 formas de interpolar variáveis em strings, a primeira é usando o sinal %, 
# a segunda é utilizando o método format e a última é utilizando o f strings.
nome, idade, profissao, linguagem, saldo = "Wagner", 31, "Programador", "Python", 45.435

print(' Utilizando o método format '.upper().center(30, '-'))
print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0}".format(nome, idade))
print()

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print()

dados = {"Name": "Sinaria", "Age": 28}
print("Nome: {Name} Idade: {Age}".format(**dados)) # Utilizanddo dicionário.
print()

print(' Utilizando f strings '.upper().center(30, '-'))
print(f"Nome: {nome} Idade: {idade}")

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
