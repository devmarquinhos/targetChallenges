# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: 
#	Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

numUser = int(input("Digite um número: ")) # Recebe o nº a ser procurado
fibPos1 = 0 # Inicio da Fibonacci sempre será em 0
fibPos2 = 1 # E o segundo termo sempre será 1

# Calcula a fibonacci enquanto o segundo termo for menor que o número a ser buscado
while fibPos2 < numUser:
    fibSum = fibPos1 + fibPos2
    fibPos1 = fibPos2
    fibPos2 = fibSum

# Verifica se o número pertence a sequência
if fibPos2 == numUser:
    print(f'O número {numUser} pertence a sequência.')
else:
    print(f'Infelizmente o número {numUser} não pertence a sequência.')