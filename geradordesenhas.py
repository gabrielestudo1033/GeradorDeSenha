import string
import random


def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = []

    for i in range(comprimento):
        caractere = random.choice(caracteres)
        senha.append(caractere)
    return ''.join(senha)

senha = gerar_senha(12)
print(senha)