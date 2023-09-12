# Os Operadores de Identidade são utilizados para comparar se os dois objetos testados ocupam a mesma posição na memória.
saldo = 1000
limite = 500
curso = "Curso de Python"
nome_curso = curso

print(saldo is limite)
print(saldo is not limite)
print(curso is nome_curso)
print(curso is not nome_curso)
