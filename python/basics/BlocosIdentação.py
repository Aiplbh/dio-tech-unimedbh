# Bootcamp DIO Geração Tech Unimed-BH - Ciência de Dados
# Modulo: Python para Ciência de Dados - Instrutor: Guilherme Carvalho
# Aplicação da aula sobre Blocos e Identação em Python


def sacar(valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado")
        print("Retire seu dinheiro.")
    if saldo < valor:
        print ("Saldo insuficiente")

sacar(400)

print ("Ação concluida. Remova o cartão")