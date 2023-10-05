'''
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
'''
altura = float(input("Insira a altura: "))
peso = 0
sexo = input("Insira o sexo do paciente Mm|Ff")
if sexo == 'M' or sexo == 'm':
    peso = (72.7 * altura) - 52
else:
    peso = (62.1 * altura) - 44.7
print(peso)