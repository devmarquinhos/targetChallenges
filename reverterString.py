# 5) Escreva um programa que inverta os caracteres de um string.
# IMPORTANTE:
#	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#	b) Evite usar funções prontas, como, por exemplo, reverse;


frase = str(input('Digite uma palavra ou uma frase: ').strip().lower()) # Recebe, retira os espaços e coloca em minúsculo
palavras = frase.split() # Separa todas as palavras
junto = ''.join(palavras) # Junta todas as palavras sem o espaço entre elas
inverso = '' # Variável para receber a string invertida

for letra in range(len(junto) -1, -1, -1): # Inverte a string letra por letra
    inverso += junto[letra]

print(frase)
print(inverso)
