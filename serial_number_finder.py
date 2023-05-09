
# This is only the root.

import re
import os
import datetime
import time
from pathlib import Path
import math
from datetime import datetime


inicio = time.time()

ruta = '' # specify the path within the ''

mi_patron = r'N\D{3}-\d{5}'

zona_horaria = '%d-%m-%Y'
fecha = datetime.now().strftime(zona_horaria)

archivos_encontrados = []
numeros_encontrados = []

def buscar_numeros(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numeros(Path(carpeta, a), mi_patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())

def mostrar_todo():
    indice = 0
    print('-' * 50)
    print(f'Fecha de busqueda: {fecha}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f'{a}\t{numeros_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros encontrados: {len(numeros_encontrados)}')
    print('-' * 50)

crear_listas()
mostrar_todo()

final = time.time()
print(f'Duración de la busqueda: {math.ceil(final - inicio)} segundos')
