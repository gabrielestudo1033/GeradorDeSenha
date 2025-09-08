import string
import random
import secrets

def gerar_senha(tamanho=12):
    # Definindo o conjunto de caracteres para a senha
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Gerando a senha de forma segura
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("Gerador de Senha Aleatória e Segura")
    tamanho = int(input("Digite o tamanho da senha desejada: "))
    
    senha_gerada = gerar_senha(tamanho)
    print(f"Senha gerada: {senha_gerada}")

    # Copiar a senha para a área de transferência
    try:
        import pyperclip
        pyperclip.copy(senha_gerada)
        print("Senha copiada para a área de transferência!")
    except ImportError:
        print("Para copiar a senha, instale o módulo pyperclip com 'pip install pyperclip'.")

if __name__ == "__main__":
    main()