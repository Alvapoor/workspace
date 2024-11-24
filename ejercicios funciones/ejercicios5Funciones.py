#Escribir dos funciones que permitan calcular:
#La cantidad de segundos en un tiempo dado en horas, minutos y segundos.
#La cantidad de horas, minutos y segundos de un tiempo dado en segundos.
#Escribe un programa principal con un menú donde se pueda elegir la opción de convertir a segundos, convertir a horas, minutos y segundos o salir del programa.
def segundos_a_hms(segundos):
  horas = segundos // 3600
  minutos = (segundos % 3600) // 60
  segundos = segundos % 60
  return horas, minutos, segundos

def hms_a_segundos(horas, minutos, segundos):
  return horas * 3600 + minutos * 60 + segundos

while True:
  print("\nMenú:")
  print("1. Convertir a segundos")
  print("2. Convertir a horas, minutos y segundos")
  print("3. Salir")

  opcion = input("Elige una opción: ")

  if opcion == "1":
    horas = int(input("Introduce las horas: "))
    minutos = int(input("Introduce los minutos: "))
    segundos = int(input("Introduce los segundos: "))
    total_segundos = hms_a_segundos(horas, minutos, segundos)
    print(f"El tiempo en segundos es: {total_segundos}")

  elif opcion == "2":
    segundos = int(input("Introduce los segundos: "))
    horas, minutos, segundos = segundos_a_hms(segundos)
    print(f"El tiempo es: {horas} horas, {minutos} minutos y {segundos} segundos")

  elif opcion == "3":
    print("Saliendo del programa...")
    break

  else:
    print("Opción inválida.")
