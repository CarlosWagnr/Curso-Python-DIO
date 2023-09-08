# Fatiamento de strings é uma técnica para retornar substrings(partes da string original), 
# informando inicio (start), fim (stop) e passo (step): [start:stop[,step]]
nome = "Carlos Wagner Alves da Conceição"

print(nome[0]) # C
print(nome[:6]) # Carlos
print(nome[7:]) # Wagner Alves da Conceição
print(nome[7:13]) # Wagner
print(nome[7:13:2]) # Wge
print(nome[:]) # Carlos Wagner Alves da Conceição
print(nome[::-1]) # oãçiecnoC ad sevlA rengaW solraC
print(nome[:-1]) # Carlos Wagner Alves da Conceiçã
print(nome[-1]) # Exibe a última letra do texto
