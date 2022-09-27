# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Estruturas de Repetição
# Comandos while , for e função built-in range
# No Python o controle da estrutura é feita por identação e sianlizada por : (dois pontos)

# Exemplo 1 - Uso do for 

print("\nExemplo 1 - Uso do for\n")

VOGAIS = "AEIOU"

texto = input("Informe um texto: ")

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end = " ")

print()

print("\nExemplo 3 - Uso do range com for\n")

# A função range(i,j,k) fornece uma sequencia de numeros inteiros
# onde o inicio é i e o fim é j-1. k é o incremento.
# o exemplo abaixo mostra como usá-la com o for
# para ver os componentes de range deve-se usá-lo com list
# list(range(4))
# >>>[0,1,2,3]
#
# range(start, stop [, step]) 

max_valor = int(input("Informe o valor máximo da lista: "))
for numero in range (0, max_valor):
    print()
    print(numero, end = " ")

print("\nExemplo 3 - Uso do while\n")

opcao = -1

while opcao != 0:
    opcao = int(input("\n[1] Saque\n[2] Extrato\n[0] Sair\n\nOpção: "))
    if opcao == 1:
        print ("Efetuando o Saque...")
    elif opcao == 2:
        print ("Emitindo extrato...")
    else:
        print("\nOperação finalizada.\n")

print("\nExemplo 4 - Uso do while com break\n")

while True: 
    escolha = int(input("\nEscolha um número de 0 a 20: "))

    if escolha == 15:
        break

print("\nNumero correto! Você saiu do loop!\n")
