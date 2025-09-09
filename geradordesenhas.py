
import tkinter as tk
from tkinter import messagebox
import string
import random
import secrets
import pyperclip

def gerar_senha(tamanho):
    if tamanho < 4:
        raise ValueError("A senha deve ter pelo menos 4 caracteres.")
    
    letras = string.ascii_letters
    digito = string.digits
    simbolos = string.punctuation

    # Garantir ao menos um de cada tipo
    senha = [
        secrets.choice(letras),
        secrets.choice(digito),
        secrets.choice(simbolos),
        secrets.choice(letras + digito + simbolos)
    ]

    todos = letras + digito + simbolos
    senha += [secrets.choice(todos) for _ in range(tamanho - 4)]
    secrets.SystemRandom().shuffle(senha)

    return ''.join(senha)

def gerar_senha_gui():
    try:
        tamanho = int(entry_tamanho.get())
        senha = gerar_senha(tamanho)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, senha)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um numero valido (minimo 4).")

def copiar_para_clipboard():
    senha = entry_resultado.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Copiado", "Senha copiada para a area de transferencia.")
    else:
        messagebox.showwarning("Aviso", "Nenhuma senha para copiar.")

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.resizable(False, False)
janela.geometry("400x200")

# Layout
label_tamanho = tk.Label(janela, text="Tamanho da Senha (min 4):")
label_tamanho.pack(pady=5)

entry_tamanho = tk.Entry(janela, width=10, justify='center')
entry_tamanho.pack()

botao_gerar = tk.Button(janela, text="Gerar Senha", command=gerar_senha_gui)
botao_gerar.pack(pady=10)

entry_resultado = tk.Entry(janela, width=40, justify="center", font=("Helvetica", 12))
entry_resultado.pack()

botao_copiar = tk.Button(janela, text="Copiar", command=copiar_para_clipboard)
botao_copiar.pack(pady=10)

# Iniciar o loop principal da interface
janela.mainloop()
