# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Strings - Interpolação
# Uso dos metodos % | format | f-string


# Declaração e inicialização de variáveis

nome = ""
profissao = ""
linguagem = ""
idade = 0


# progam title

print ("\nIntepolação de strings - % | format | f-string")
print ("==============================================\n\n")


# Data input

nome = input ("Informe seu nome: ")
idade = int(input ("Informe sua idade: "))
profissao = input ("Informe sua profissão: ")
linguagem = input ("Informe Linguagem: ")
saldo = 45.554


# Process

print ("\nFormating ...")
print ("\n1) Usando operador % --> "+ 'print ("Nome: %s Idade: %d" %(nome,idade))')
#print ('print ("Nome: %s Idade: %d" %(nome,idade))')
print ("Nome: %s Idade: %d" %(nome,idade))


print()

print ("\n2) Usando o metodo .format --> "+ 'print ("Nome: {} Idade: {}" .format(nome,idade))')
print ("Nome: {0} Idade: {1}" .format(nome,idade))

print()

print ("\n3) Usando o metodo .format --> "+ 'print ("Nome: {0} Idade: {1}" .format(nome,idade))')
print ("Nome: {0} Idade: {1}" .format(nome,idade))

print()

print ("\n4) Usando o metodo .format --> "+ 'print ("Nome: {name} Idade: {age}" .format(name=nome,age=idade))')
print ("Nome: {name} Idade: {age}" .format(name=nome,age=idade))

print()

# Usando dicionario de dados

dados = {"nome": "Aipl", "idade" : 28}

print ('Dicionario criado: dados = {"nome": "Aipl", "idade" : 28}')
print ("\n5) Usando o metodo .format com dicionario de dados --> "+ 'print (**dados))')
print ("Nome: {nome} Idade: {idade}" .format(**dados))

print()

print ("\n6) Usando o metodo f-strngs --> "+ 'print (f"Nome: {nome} Idade: {idade}")')
print ("Nome: {nome} Idade: {idade}")

print ("\n7) Usando formatação com f-string --> "+ 'print (f"Nome: {nome} Idade: {idade} Saldo: {saldo: 2.2f}"')
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo:2.2f}")

print()

print ("\n8) Usando formatação com f-string --> "+ 'print (f"Nome: {nome} Idade: {idade} Saldo: {saldo: 2.1f}"')
print (f"Nome: {nome} Idade: {idade} Saldo: {saldo:2.1f}")

print ()
