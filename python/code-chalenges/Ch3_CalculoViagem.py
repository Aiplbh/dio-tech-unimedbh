# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

# Desafio 3 - Cálculo do consumo de combustível em uma viagem

# O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas 
# e o segundo é a velocidade média durante a mesma em km/h.

# Consumo de combustível veicular de Rubens (12 km/l)
CONSUMO_VEICULAR = 12 

# Input validation
validacao = False

while (not validacao):

    entrada = input().split(" ")

    tempo_de_viagem   = int(entrada[0])
    velocidade_media  = int(entrada[1])
    

    if tempo_de_viagem <= 0 :
        teste_tempo = False
        print ("Tempo de viagem inválido")
    else:
        teste_tempo = True   

    if  velocidade_media == 0:
        teste_velocidade = False
        print ("Velocidade media inválida")
    else:
        teste_velocidade = True
        

    if teste_velocidade and teste_tempo:
        validacao = True
    else:
        validacao = False

    entrada = ""   


# TODO: Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal

# Total distance (km)
distancia_percorrida = tempo_de_viagem * velocidade_media

# Fuel_consumption Calculation (em litros)

gasto_de_combustivel = distancia_percorrida / CONSUMO_VEICULAR

# Output
print (f"{gasto_de_combustivel:.3f}")

