#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# 	SP – R$67.836,43
# 	RJ – R$36.678,66
# 	MG – R$29.229,88
# 	ES – R$27.165,48
# 	Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

SP = 67836.43
RJ = 36678.66
MG = 29229.88
ES = 27165.48
outros = 19849.53

faturamentoTotal = SP + RJ + MG + ES + outros

print(f'São Paulo: {(SP * 100) / faturamentoTotal}%')
print(f'Rio de Janeiro: {(RJ * 100) / faturamentoTotal}%')
print(f'Minas Gerais: {(MG * 100) / faturamentoTotal}%')
print(f'Espirito Santo: {(ES * 100) / faturamentoTotal}%')
print(f'Outros: {(outros * 100) / faturamentoTotal}%')

