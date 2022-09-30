# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Estruturas condicionais
# if | if .. else | if ternário

# Exemplo 1 - Usando apenas if 

saldo = 2000.0

saque = float(input("\nSaque 1: Informe o valor do saque: "))

if saldo >= saque:
    print("Estamos providenciando sua solicitação")

if saldo < saque:
    print ("Saldo insuficiente")


# Exemplo 2 - Usando if..else  
saque = float(input("\nSaque 2: Informe o valor do saque: "))

if saldo >= saque:
    print("Estamos providenciando sua solicitação")
else:
    print ("Saldo insuficiente")


# Exemplo 3 - Usando if..elif..else 


print("\n-----------------------------\n")

opcao = int(input ("Digite sua opção\n\n[1] Saque \n[2] Extrato\n\nOpção: "))

if opcao == 1:
    print("\nEstamos providenciando sua solicitação")

elif opcao == 2:
    print("\nGerando seu extrato. Aguarde...")

else: 
    print ("\nValor inválido. Cancelando a operação") 

print("\n-----------------------------\n")


# Exemplo 4 - if ternario

CODIGO_CARTAO = 50063578

cartao_usuario = int(input("Informe o número do cartão com oito digitos: "))

status = "Cartão válido." if CODIGO_CARTAO == cartao_usuario else "Cartão invalido."

print (f"\nStatus do usuário: {status}")


print("\nObrigado por usar nossos serviços!\n")