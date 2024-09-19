# 1) Cálculo do valor da variável SOMA
def calcula_soma():
    INDICE = 13
    SOMA = 0
    K = 0
    while K < INDICE:
        K += 1
        SOMA += K
    print(f"O valor final de SOMA é {SOMA}.")

# 2) Verificar se um número pertence à sequência de Fibonacci
def fibonacci(n):
    if n < 0:
        return f"O número {n} não pertence à sequência de Fibonacci."

    a, b = 0, 1
    while a <= n:
        if a == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} não pertence à sequência de Fibonacci."

def verifica_fibonacci():
    numero = int(input("Informe um número: "))
    print(fibonacci(numero))

# 3) Cálculo de valores de faturamento diário
def calcula_faturamento_diario():
    faturamento_diario = {
        "faturamento": [1000, 1500, 0, 2000, 2500, 0, 0, 3000, 3200, 2800]
    }

    dias_com_faturamento = [dia for dia in faturamento_diario["faturamento"] if dia > 0]

    menor_valor = min(dias_com_faturamento)
    maior_valor = max(dias_com_faturamento)
    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_da_media = len([dia for dia in dias_com_faturamento if dia > media_mensal])

    print(f"Menor valor: R$ {menor_valor}")
    print(f"Maior valor: R$ {maior_valor}")
    print(f"Dias acima da média: {dias_acima_da_media}")

# 4) Cálculo do percentual de faturamento por estado
def calcula_percentual_faturamento_estados():
    faturamento_estados = {
        'SP': 67836.43,
        'RJ': 36678.66,
        'MG': 29229.88,
        'ES': 27165.48,
        'Outros': 19849.53
    }

    faturamento_total = sum(faturamento_estados.values())

    for estado, valor in faturamento_estados.items():
        percentual = (valor / faturamento_total) * 100
        print(f"{estado}: {percentual:.2f}% do faturamento total")

# 5) Inversão de uma string
def inverter_string():
    texto = input("Digite uma string: ")
    invertida = ""
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    print(f"String invertida: {invertida}")

# Função principal para escolher qual parte do código executar
def main():
    while True:
        print("\nEscolha a função que deseja executar:")
        print("1 - Calcular soma (Questão 1)")
        print("2 - Verificar número na sequência de Fibonacci (Questão 2)")
        print("3 - Calcular faturamento diário (Questão 3)")
        print("4 - Calcular percentual de faturamento por estado (Questão 4)")
        print("5 - Inverter string (Questão 5)")
        print("0 - Sair")
        
        escolha = input("Digite o número da função: ")

        if escolha == '1':
            calcula_soma()
        elif escolha == '2':
            verifica_fibonacci()
        elif escolha == '3':
            calcula_faturamento_diario()
        elif escolha == '4':
            calcula_percentual_faturamento_estados()
        elif escolha == '5':
            inverter_string()
        elif escolha == '0':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa principal
if __name__ == "__main__":
    main()
