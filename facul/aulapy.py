numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceio número: '))
numero4 = int(input('Digite o quarto número: '))

somar = numero1 + numero2 + numero3 + numero4
subtrair = numero1 - numero2 - numero3 - numero4
multiplicar = numero1 * numero2 * numero3 * numero4
dividir = numero1 / numero2 / numero3 / numero4
media = somar / 4

print(f'A soma deles é {somar}')
print(f'A subtração deles é {subtrair}')
print(f'A multiplicação dele é {multiplicar}')
print(f'A divisão deles é {dividir:.2}')
print(f'A média deles é {media}')

if somar % 2 == 0: 
    print('O número da soma é PAR')
else:
    print('O número da soma é IMPAR')

if subtrair < 0:
    print('A subtração é negativa')
else:
    print('A subtração é positiva')

if multiplicar > 100 and multiplicar < 1000:
    print('O resultado da multiplicação está entre 100 e  1000')
else: 
    print('O resultado da multiplicação não está entre 100 e  1000')

if dividir > 0:
    print('A divisão é maior que 0')
else:
    print('A divisão é menor que 0')
