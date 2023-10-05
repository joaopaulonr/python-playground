# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
sum = 0
for i in range(4):
    nota = float(input("Insira uma nota: "))
    sum = sum + nota
average = sum / 4
print(average)