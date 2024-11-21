letra = input('Dime una letra: ')
def abecedario(a):
    vocales = 'uaioe'
    return a in vocales
result= abecedario(letra)

print(f'¿La letra es una vocal? {result}')