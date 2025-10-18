def verificar_tamanho_senha():
    """
    Solicita uma senha ao usuário e verifica se ela possui pelo menos 8 caracteres.
    """
    
    print("--- Verificador de Segurança de Senha (Tamanho) ---")
    
    # 1. Solicita a senha ao usuário
    # Usamos input() para obter a senha
    senha = input("Digite a senha que deseja verificar: ")
    
    # 2. Define o critério mínimo
    TAMANHO_MINIMO = 8
    
    # 3. Verifica o tamanho da senha
    # len() retorna o número de caracteres na string
    tamanho_atual = len(senha)
    
    print(f"A senha digitada tem {tamanho_atual} caracteres.")
    
    # 4. Aplica a lógica condicional
    if tamanho_atual >= TAMANHO_MINIMO:
        print("\n✅ OK! A senha atende ao critério de ter pelo menos 8 caracteres.")
    else:
        # Calcula quantos caracteres faltam
        faltam = TAMANHO_MINIMO - tamanho_atual
        print(f"\n❌ FALHA! A senha é muito curta.")
        print(f"Ela precisa de pelo menos {TAMANHO_MINIMO} caracteres. Faltam {faltam} caracteres.")
        
    print("--------------------------------------------------")

# Executa a função principal
if __name__ == "__main__":
    verificar_tamanho_senha()