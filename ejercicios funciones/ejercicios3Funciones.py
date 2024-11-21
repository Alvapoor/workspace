#3. Definir una funcion llamada histograma() que tome una lista de números enteros e imprima un histograma en la pantalla. 


def histograma(repeticiones):
    
    for numero in repeticiones:
        print('x' * int(numero))

repeticiones = input('Ingrese los numeros separados por comas : ').split()

