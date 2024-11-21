def max_de_tres(a, b, c):
  if a > b:
    if a > c:
      return a
    else:
      return c
  else:
    if b > c:
      return b
    else:
      return c

numero1 = int(input('Dime el primer numero: '))
numero2 = int(input('Dime el segundo numero: '))
numero3 = int(input('Dime el tercer numero: '))

mayor = max_de_tres(numero1, numero2, numero3)
print(f"El mayor de {numero1}, {numero2} y {numero3} es: {mayor}")
