# Estrutura de repetição são utilizadas para um trecho de código para serem executados um determinado número de vezes.
# O comando 'for' para percorrer um objeto interável, faz sentido usarmos quando sabemos o número exato de vezes que o bloco de código deve executar.
#texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=", ")
else:
    print()
    print("Executa no final do laço.")


# Exemplo utilizando a função built-in range
print()
for numero in range(0, 51, 5):
    print(numero, end=" ")