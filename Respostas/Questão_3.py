Programa para calcular valores de faturamento diário

import json

# Exemplo de dados fictícios de faturamento
faturamento_diario = {
    "faturamento": [1000, 1500, 0, 2000, 2500, 0, 0, 3000, 3200, 2800]
}

# Calculando o menor e maior valor de faturamento
menor_valor = min(filter(lambda x: x > 0, faturamento_diario["faturamento"]))
maior_valor = max(faturamento_diario["faturamento"])

# Calculando a média mensal
dias_com_faturamento = [dia for dia in faturamento_diario["faturamento"] if dia > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contando o número de dias acima da média mensal
dias_acima_da_media = len([dia for dia in dias_com_faturamento if dia > media_mensal])

print(f"Menor valor: R$ {menor_valor}")
print(f"Maior valor: R$ {maior_valor}")
print(f"Dias acima da média: {dias_acima_da_media}")
