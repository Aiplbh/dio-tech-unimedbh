# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar

# Desafio 2 - Hot-dogs

# Input
#from operator import and_




# Input validation
validacao = False

while (not validacao):

    entrada = input().split(" ")

    total_hotdogs        = int(entrada[0])
    total_participantes  = int(entrada[1])
    

    if total_hotdogs <= 0 :
        teste_hotdogs = False
        print ("Total de Hot-Dogs inválido")
    else:
        teste_hotdogs = True   

    if  total_participantes > 1000 :
        teste_participantes = False
        print ("Total de Participantes inválido")
    else:
        teste_participantes = True
        

    if teste_hotdogs and teste_participantes:
        validacao = True
    else:
        validacao = False

    entrada = ""   

# print (entrada)
# print (total_hotdogs)
# print (total_participantes)


# Media_Hot_Dogs Calculation
media_hot_dogs = total_hotdogs / total_participantes

# Output
print (f"{media_hot_dogs:.2f}")