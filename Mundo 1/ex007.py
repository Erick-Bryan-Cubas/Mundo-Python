# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
primeira_nota = float(input('Qual a primeira nota do discente? '))
segunda_nota = float(input('Qual a segunda nota do discente? '))
nota_media = ((primeira_nota + segunda_nota)/2)

if (nota_media < 6):
    print('Discente com nota {}, reprovado!'.format(nota_media))
elif (nota_media == 6 or nota_media <7):
    print('Discente com nota {}, aceitável'.format(nota_media))
else:
    print('Discente com {}, excelente!'.format(nota_media))