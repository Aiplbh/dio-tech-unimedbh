def imprime_dados_reajuste (novo_salario, reajuste):
   print("Novo salario: {:.2f}".format(novo_salario))
   print("Reajuste ganho: {:.2f}".format(reajuste))
   print(f"Em percentual: {round(percentual)} %\n")
   
   # Listagem de saida inline
   # print("Novo salario: {:.2f} Reajuste ganho: {:.2f}".format(novo_salario, reajuste) ,f" Em percentual: {round(percentual)} %\n")

salario = float(input()) 

# Regra do reajuste
if (salario > 2000 ): 
    novo_salario = salario * 1.05
    percentual = 5

elif (salario >= 1500):
    novo_salario = salario * 1.10
    percentual = 10

elif (salario >= 900):
    novo_salario = salario * 1.12
    percentual = 12


elif (salario > 600):
    novo_salario = salario * 1.13
    percentual = 13

else: 
    novo_salario = salario * 1.17
    percentual = 17

reajuste = novo_salario - salario

imprime_dados_reajuste(novo_salario, reajuste)