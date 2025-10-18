def registrar_e_calcular_media():
    """
    Registra as notas de alunos, armazena em uma lista e calcula a média da turma.
    """
    
    # Lista para armazenar as notas de todos os alunos
    notas_da_turma = []
    
    print("--- Sistema de Registro de Notas da Turma ---")
    
    # 1. Obter o número de alunos na turma
    while True:
        try:
            num_alunos = int(input("Quantos alunos há na turma? "))
            if num_alunos > 0:
                break
            else:
                print("O número de alunos deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
            
    # 2. Loop para registrar as notas de cada aluno
    for i in range(num_alunos):
        print(f"\n--- Aluno {i + 1} de {num_alunos} ---")
        
        # Obter o nome do aluno (opcional, mas bom para registro)
        nome_aluno = input(f"Digite o nome do aluno {i + 1}: ")
        
        # Obter e validar a nota
        while True:
            try:
                # Usamos float para permitir notas com casas decimais (ex: 8.5)
                nota = float(input(f"Digite a nota de {nome_aluno}: "))
                # Simples validação de nota (ex: 0 a 10)
                if 0 <= nota <= 10: 
                    break
                else:
                    print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
        
        # Adiciona a nota à lista principal
        notas_da_turma.append(nota)
        
    # 3. Calcular a Média da Turma
    
    if not notas_da_turma:
        # Caso não tenha sido registrada nenhuma nota (o que é improvável dado o loop anterior,
        # mas bom para segurança)
        print("\nNenhuma nota foi registrada. A média não pode ser calculada.")
        return

    # Soma todas as notas da lista
    soma_das_notas = sum(notas_da_turma)
    
    # Calcula a média
    media_da_turma = soma_das_notas / len(notas_da_turma)
    
    # 4. Exibir o Resultado
    
    print("\n==================================")
    print("RESUMO DA TURMA")
    print(f"Total de alunos registrados: {len(notas_da_turma)}")
    print(f"Soma total das notas: {soma_das_notas:.2f}")
    print(f"Média da Turma: {media_da_turma:.2f}")
    print("==================================")

# Executa a função principal
if __name__ == "__main__":
    registrar_e_calcular_media()