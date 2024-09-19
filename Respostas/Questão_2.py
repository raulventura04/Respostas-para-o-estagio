
2.Programa para verificar se um número pertence à sequência de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return f"O número {n} pertence à sequência de Fibonacci."
        a, b = b, a + b
    return f"O número {n} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(fibonacci(numero))
