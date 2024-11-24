#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor
def Login(nombre_usuario, contrasena, intentos):

  if nombre_usuario == "usuario1" and contrasena == "asdasd":
    return True
  else:
    intentos += 1
    return False

intentos = 0
max_intentos = 3

while intentos < max_intentos:
  nombre_usuario = input("Ingresa tu nombre de usuario: ")
  contrasena = input("Ingresa tu contraseña: ")

  if Login(nombre_usuario, contrasena, intentos):
    print("Inicio de sesión exitoso.")
    break
  else:
    print(f"Inicio de sesión fallido. Intentos restantes: {max_intentos - intentos}")

if intentos == max_intentos:
  print("Número máximo de intentos alcanzado.")
