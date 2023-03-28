# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
num = int(input('Digite um número: '))
dobro = pow(num, 2)
triplo = pow(num, 3)
raiz_quadrada = pow(num, 0.5)
print('O número digitado é: {} \n seu dobro: {} \n triplo: {} \n e raiz quadrada: {} '.format(num, dobro, triplo, raiz_quadrada))