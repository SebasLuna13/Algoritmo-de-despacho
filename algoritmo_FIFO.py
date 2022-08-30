import numpy as np
import matplotlib.pyplot as plt

#Listas
lista_procesos = []
procesos_ordenados = []

#Inicio codigo
print('\n+------------------------------------------------------------------+')
print('|                    Algoritmo De Despacho FIFO                    |')
print('+------------------------------------------------------------------+')
cant_procesos = int(input('|  Ingrese el numero de procesos con los que desea trabajar: '))
print('+------------------------------------------------------------------+')

for i in range(cant_procesos):
    nombre_proceso = input(f'|  Ingrese el nombre del proceso {i + 1}: ') 
    rafaga_proceso = int(input(f'|  Ingrese la rafaga del proceso {i + 1}: '))
    tiempo_proceso = int(input(f'|  Ingrese el tiempo del proceso {i + 1}: '))
    print('+------------------------------------------------------------------+')
    lista_procesos.append([nombre_proceso, rafaga_proceso, tiempo_proceso])

print('\n')
# Codigo de Ordenamiento por prioridad
lista_procesos = sorted(lista_procesos, key=lambda proceso : proceso[2])

print('+---------------Tabla de Datos---------------+')

print('\n+-------------------------+')
print('| Proceso | Rafaga | Time |')
print('+-------------------------+')
for i in lista_procesos:
    print(f'| {i[0]} |  {i[1]}  |  {i[2]}  |')
    print('+-------------------------+')

print('\n')

#------------------------------------------------------------------------------------
#Procesos Ordenados una vez aplicado el algoritmo de desempeño FIFO

for i in range(cant_procesos):
    if i == 0:
        procesos_ordenados.append([lista_procesos[0][0], 0, lista_procesos[0][1]])
        procesos = lista_procesos[i][1]
    else:
        procesos_ordenados.append([lista_procesos[i][0], procesos, procesos + lista_procesos[i][1]])
        procesos = procesos + lista_procesos[i][1]

print('+---------------Tabla Ordenamiento ---------------+')

print('\n+-------------------------+')
print('| Proceso | Rafaga | Time |')
print('+-------------------------+')
for i in procesos_ordenados:
    print(f'| {i[0]} |  {i[1]}  |  {i[2]}  |')
    print('+-------------------------+')

print('\n')

#------------------------------------------------------------------------------------
# Cálculo del Tiempo de Espera TE
tiempo_espera = 0
for i in range(cant_procesos):
    tiempo_espera = tiempo_espera + (procesos_ordenados[i][1] - lista_procesos[i][2])

tiempo_espera = tiempo_espera / cant_procesos

print("El tiempo de espera: " , tiempo_espera)

#------------------------------------------------------------------------------------
# Cálculo de Tiempo del Sistema TS

tiempo_sistema = 0
for i in range(cant_procesos):
    tiempo_sistema = tiempo_sistema + (procesos_ordenados[i][2] - lista_procesos[i][2])

tiempo_sistema = tiempo_sistema /cant_procesos

print("\nEl tiempo de sistema: ", tiempo_sistema)
print('\n')