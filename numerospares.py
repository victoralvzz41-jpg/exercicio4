def analisar_e_contar_numeros():
    """
    Solicita números ao usuário até que ele decida parar, classifica
    e conta quantos números são pares e quantos são ímpares.
    """

    # Contadores para armazenar os totais
    total_pares = 0
    total_impares = 0
    
    print("--- Analisador de Números: Par ou Ímpar ---")
    print("Digite 'sair' a qualquer momento para ver o resultado.")

    # Loop principal para coletar os números
    while True:
        entrada = input("Digite um número inteiro ou 'sair' para finalizar: ").strip().lower()

        # Verifica se o usuário quer sair
        if entrada == 'sair':
            break
        
        # Tenta converter a entrada para um número inteiro
        try:
            numero = int(entrada)
            
            # Lógica para classificar Par ou Ímpar
            # Um número é par se o resto da divisão por 2 for 0 (numero % 2 == 0)
            if numero % 2 == 0:
                print(f"-> O número {numero} é PAR.")
                total_pares += 1  # Incrementa o contador de pares
            else:
                print(f"-> O número {numero} é ÍMPAR.")
                total_impares += 1 # Incrementa o contador de ímpares
                
        except ValueError:
            # Captura o erro se o usuário digitar algo que não é 'sair' nem um número
            print("Entrada inválida. Por favor, digite um número inteiro ou 'sair'.")

    # Exibe o resultado final
    print("\n==================================")
    print("RESUMO DA ANÁLISE")
    print(f"Total de números inseridos: {total_pares + total_impares}")
    print(f"Números Pares: {total_pares}")
    print(f"Números Ímpares: {total_impares}")
    print("==================================")

# Executa a função principal
if __name__ == "__main__":
    analisar_e_contar_numeros()