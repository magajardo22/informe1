import random
import time
from math import log

inicio_intervalo = 1
cantidad_datos = 10000


datos = [random.randint(1, 99) for i in range(cantidad_datos)]
rango=max(datos)-min(datos)
cantidad_intervalos=1+3.322*log(cantidad_datos)
amplitud=rango/round(cantidad_intervalos)

def crear_lista_intervalos(cantidad_intervalos, inicio_intervalo):
    intervalos = []
    for i in range(round(cantidad_intervalos)):
        intervalo = (inicio_intervalo, inicio_intervalo + round(amplitud)-1)
        intervalos.append(intervalo)
        inicio_intervalo += round(amplitud)
    return intervalos

lista_intervalos = crear_lista_intervalos(cantidad_intervalos, inicio_intervalo)

def contar_frecuencia(datos, intervalos):
    histograma = {intervalo: 0 for intervalo in intervalos}
    
    for valor in datos:
        for intervalo in intervalos:
            if intervalo[0] <= valor <= intervalo[1]:
                histograma[intervalo] += 1
    return histograma

def main():
    iniciotime = time.time()
    histograma = contar_frecuencia(datos, lista_intervalos)

    for intervalo, frecuencia in histograma.items():
        print(f"Intervalo {intervalo}: {frecuencia} datos")

    fintime = time.time()
    resultadotime=fintime-iniciotime
    print(resultadotime)

if __name__ == '__main__':
    main()
