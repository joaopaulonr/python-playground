'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''
def descontos(salario_bruto):
    imposto_renda = 0.11 * salario_bruto
    inss = 0.08 * salario_bruto
    sindicato = 0.05 * salario_bruto
    salario_liquido = salario_bruto - imposto_renda - inss - sindicato
    print(f"+ Salario bruto: {salario_bruto} \n- IR (11%): {imposto_renda}\n- INSS (8%): {inss}\n- Sindicato (5%): {sindicato}\n= Salario liquido: {salario_liquido}")

descontos(1000)