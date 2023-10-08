"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

def tempoDowload(arquivo,velocidade):
    MBs = velocidade / 8
    tempo_segundos = arquivo / MBs
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos
    

arquivo = float(input("Insira o tamanho do arquivo em MB: "))
velocidade = float(input("Insira a velocidade em mbps: "))

tempo = tempoDowload(arquivo,velocidade)
print(f"O tempo necessário para download é de {tempo:.2f}min")