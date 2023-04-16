# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#	• O menor valor de faturamento ocorrido em um dia do mês;
#	• O maior valor de faturamento ocorrido em um dia do mês;
#	• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#	a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#	b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import pandas as pd # Biblioteca Pandas para fazer análise

jsonDir = "dados.json" # Endereço do json

# Carrega os dados do json em um dataframe e também coleta o menor valor e o maior valor.
df = pd.DataFrame(pd.read_json(jsonDir))
valorMin = df.min().min()
valorMax = df.max().max()

# Cálcula a média dos valores desconsiderando os dias em que o valor foi zero
media = df[df['valor'] != 0]['valor'].mean()

# Conta a quantidade de dias acima da média
acimaMedia = (df['valor'] > media).sum()

print(df)
print(f'\nO menor valor foi: {valorMin}')
print(f'O maior valor foi: {valorMax}')
print(f'A média foi: {media}')
print(f'Dias acima da média foi: {acimaMedia}')
