# Strings de multiplas linhas são definidas informando 3 aspas simples ou duplas durante a atribuição. 
# Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.
nome = "Wagner"

mensagem = f"""
    Olá meu nome é {nome},
  Eu estou aprendendo Python,
      Essa mensagem tem diferentes recursos.
"""

print(mensagem)

print("""
    ============= MENU =============
    1 - Depositar
    2 - Sacar
    3 - Sair
    ================================
            Obrigado por utilizar nosso sistema!
""")