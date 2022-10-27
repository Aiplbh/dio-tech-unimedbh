# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

# Desafio 1 - Duas Torres

# Input
from operator import and_




# Input validation
validacao = False

while (not validacao):

    entrada = input().split(" ")

    distancia_entre_palantirs = int(entrada[0])
    diametro_palantir_sauron  = int(entrada[1])
    diametro_palantir_saruman = int(entrada[2])

    if distancia_entre_palantirs < 0 or distancia_entre_palantirs > 10000:
        teste_distancia = False
        print ("Distancia entre Palatirs inválida")
    else:
        teste_distancia = True   

    if  diametro_palantir_sauron > 0 :
        teste_diametro_sauron = True
    else:
        teste_diametro_sauron = False
        print ("Diametro Palatir Sauron inválido")


    if  diametro_palantir_saruman < 100 :
        teste_diametro_saruman = True
    else:
        teste_diametro_saruman = False
        print ("Diametro Palatir Saruman inválido")

    if teste_distancia and teste_diametro_saruman and teste_diametro_sauron:
        validacao = True
    else:
        validacao = False

    entrada = ""   

# print (entrada)
# print (distancia_entre_palantirs)
# print (diametro_palantir_sauron)
# print (diametro_palantir_saruman)


# TODO: Calcule o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais no espaço #em branco abaixo:

# ICM Calculation
icm = distancia_entre_palantirs / (diametro_palantir_sauron  + diametro_palantir_saruman)

# Output
print (f"{icm:.2f}")