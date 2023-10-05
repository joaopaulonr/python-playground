'''
 Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
 o produto do dobro do primeiro com metade do segundo .
 a soma do triplo do primeiro com o terceiro.
 o terceiro elevado ao cubo.
 '''
def operations(num1,num2,num3):
    operation1 = (num1*2)*(num2 / 2)
    operation2 = (num1*3)+ num3
    operation3 = num3**3
    print(operation1,operation2, operation3)

operations(1,2,3.4)