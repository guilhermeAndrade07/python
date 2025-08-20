# Crie um programa que simule uma senha de 4 dígitos. O usuário tem 3 tentativas para acertar


senha_secreta = '1234'

# Inicializa o contador de tentativas
tentativas = 0
max_tentativas = 3

print("Bem-vindo ao simulador de senha!")
print(f"Você tem {max_tentativas} tentativas para adivinhar a senha de 4 dígitos.")


while tentativas < max_tentativas:
    palpite = input(f"Tentativa {tentativas + 1}: Digite a senha de 4 dígitos: ")

    if palpite == senha_secreta:
        print("Parabéns! Você acertou a senha!")
        break
    else:
        print("Senha incorreta.")
    
    tentativas += 1
    
# Verifica se o loop terminou por esgotar as tentativas (não por 'break')
if tentativas == max_tentativas:
    print("\nSuas tentativas acabaram.")
    print(f"A senha correta era: {senha_secreta}")