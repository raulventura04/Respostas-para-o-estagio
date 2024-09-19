Programa para calcular percentuais de faturamento por estado

faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total
faturamento_total = sum(faturamento_estados.values())

# Calculando o percentual de cada estado
for estado, valor in faturamento_estados.items():
    percentual = (valor / faturamento_total) * 100
    print(f"{estado}: {percentual:.2f}% do faturamento total")
