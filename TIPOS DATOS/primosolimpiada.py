#programa que decide si un número es primo o no y que calcula un número de primos consecutivos.
t = int(input('indica el numero de casos que hace falta procesar'))
for i in range(0,t):
    k = int(input('Introduce un numero entre 0 y 100: '))
    n = int(input('Introduce un numero entero entre 1 y 100000: '))
    if k==0:
        if !(n % 2 ):
            print('NO')
        else:
            print('SI')
