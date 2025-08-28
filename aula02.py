numero_secreto = 20


















numero = int(input('Digite um número: '))

if numero == numero_secreto:
    print('Parabens, você acertou!!')
else:
    if numero > numero_secreto:
        print('É menor...')
    else:
        if numero < numero_secreto:
            print('É maior...')
        else:
            print('Você errou')