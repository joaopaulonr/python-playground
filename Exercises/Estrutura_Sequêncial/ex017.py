"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

def quantidade(area):
    qtd_latas = math.ceil((area / 6) / 18)
    valor_latas = qtd_latas * 80.0
    galao_area_pintada = math.ceil((area / 6) / 3.6)
    valor_galao = galao_area_pintada * 25.0

    tinta_restante = (area / 6) % 18
    print (tinta_restante)

    #print(f"Para a área de {area}m²\nquantidade de latas: {lata_area_pintada}\nValor total: {valor_lata}\nQuantidade de galões: {galao_area_pintada}\nValor total: {valor_galao:.2f}")

area = float(input("Insira a área a ser pintada: "))

quantidade(area)