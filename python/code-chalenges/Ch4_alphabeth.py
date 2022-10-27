# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;


# Desafio
# Dada a letra N do alfabeto, nos diga qual a sua posição.

# Entrada
# Um único caracter N, uma letra maiúscula ('A'-'Z') do alfabeto (que contém 26 letras).

# Saída
# Um único inteiro, que representa a posição da letra no alfabeto.


# letras_maiusculas = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]
# letras_minusculas = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
#                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

# [ABCDEFGHIJKLMNOPQRSTUVWXYZ]
# [abcdefghijklmnopqrstuvwxyz]


# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;

lower_case_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# 1) Receber dado de entrada
letter = input() 

# 2) iterar a lista do início até a letra fornecida e compara com o valor fornecido
#    imprimindo o valor do item quando encontrar a letra digitada.

for item in lower_case_alphabet:
    if (item == letter):
        print (lower_case_alphabet.index(item)+ 1)


for item in upper_case_alphabet:
    if (item == letter):
        print (upper_case_alphabet.index(item)+ 1)









