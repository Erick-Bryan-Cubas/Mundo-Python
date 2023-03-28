# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor. 
num = int(input('Digite um número: '))
antecessor = num - 1
sucessor = num + 1
print('O número digitado foi {} sendo o antecessor e sucessor: {} e {}'.format(num, antecessor, sucessor))
