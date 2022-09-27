# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Manipulação de strings com Python

# Uso dos metodos .upper(), .()lower e .title()

from platform import python_branch


print ("\nExemplo 1 - Uso de lowercase, uppercase e title\n")
print ("-----------------------------------------------\n")
#============================================================

nome = input("\nEntre com uma string: ")

print (f"\nUsando o método upper(): {nome.upper()}")
print (f"\nUsando o método lower(): {nome.lower()}")
print (f"\nUsando o método title(): {nome.title()}")

input("\nEnter para o exemplo 2: ")

print ("\nExemplo 2 - Uso de strip para remoção de espaço")
print ("-----------------------------------------------\n")
#===============================================================

texto = "      Olá mundo!          "

# print ("\nRemoção dos espaços em branco com strip\n")
print(f"String original: |{texto}|\n")
print(f"String sem espaços: |{texto.strip()}|\n")
print(f"String sem espaços a direita: |{texto.rstrip()}|\n")
print(f"String sem espaços a esquerda: |{texto.lstrip()}|\n")

input("\nEnter para o exemplo 3: ")

print ("\nExemplo 3 - Uso do metodo .center()")
print ("---------------------------------\n")
#================================================
menu = "Python"
centro = -1

while centro != 0:
    centro=int(input("\nEntre com um valor para centralizar a palavra Python: "))
    print()
    print (menu.center(centro,"_"))

print("\nImpossível centralizar para o valor informado\n")

input("\nEnter para o exemplo 4: ")

print ("\nExemplo 4 - Uso do metodo .join()")
print ("---------------------------------\n")
#=============================================

separador = " "

while separador != "":
    palavra = input ("\nInforme uma palavra: ")
    separador = input("\nInforme um caracter separador: ")
    print()
    print (separador.join(palavra))

print("\nCaracter separador não informado\n")

