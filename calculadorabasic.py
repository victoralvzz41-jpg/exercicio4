# 1. Definição das Funções para as Operações
def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    # Tratamento para evitar o erro de divisão por zero
    if n2 == 0:
        return "Erro: Divisão por zero não é permitida."
    return n1 / n2

def calculadora():
    """Função principal que gerencia a entrada, a escolha da operação e a saída."""
    
    print("--- Calculadora Python ---")
    print("Selecione a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("--------------------------")

    # 2. Loop principal para a escolha da operação
    while True:
        escolha = input("Digite a opção (1/2/3/4): ")

        # Verifica se a escolha é válida
        if escolha in ('1', '2', '3', '4'):
            break
        else:
            print("Opção inválida. Tente novamente.")

    # 3. Solicita os números
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")

    # 4. Executa a operação e exibe o resultado
    if escolha == '1':
        resultado = somar(num1, num2)
        simbolo = '+'
    elif escolha == '2':
        resultado = subtrair(num1, num2)
        simbolo = '-'
    elif escolha == '3':
        resultado = multiplicar(num1, num2)
        simbolo = '*'
    elif escolha == '4':
        resultado = dividir(num1, num2)
        simbolo = '/'
        
    print(f"\nResultado:")
    
    # Verifica se o resultado é uma string de erro ou um número
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"{num1} {simbolo} {num2} = {resultado:.2f}")

# Executa a função
if __name__ == "__main__":
    calculadora()