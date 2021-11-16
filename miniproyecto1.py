import random


nombre=input("Ingresa tu nombre:\n")

print("\n")
print("Hola "+nombre+". Juguemos un juego. Yo pensare en un numero del 1 al 100 y tu intentaras adivinarlo.")

numero=random.randint(1,100)
usuario=-1
intentos=0

while usuario!=0 and usuario!=numero:
  print("\n")
  usuario=int(input("Ingresa el numero entre 1 y 100 que crees que estoy pensando (0 para parar).\n"))
  print("\n")
  if usuario>0:
    if usuario==numero:
      print("Felicitaciones "+nombre+", el numero en el que estaba pensando era "+str(numero)+". Lo lograste en "+str(intentos)+" intentos.")
    elif abs(usuario-numero)>20:
      intentos=intentos+1
      print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 20.")
    elif 20>=abs(usuario-numero)>10:
      intentos=intentos+1
      print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 10 y menor o igual a 20.")
    elif 10>=abs(usuario-numero)>5:
      intentos=intentos+1
      print("Sorry "+nombre+", ese no es pero estas a una distancia mayor que 5 y menor o igual a 10.")
    elif 5>=abs(usuario-numero):
      intentos=intentos+1
      print("Sorry "+nombre+", ese no es pero estas a una distancia menor o igual a 5.")
  elif usuario<0:
    print("Debes ingresar un valor positivo entre 1 y 100, pero no te preocupes, no contaremos este intento.")
  else:
    print("No lo lograste "+nombre+", a pesar de tratar "+str(intentos)+" veces. Mas suerte para otra vez.")
  
print("\n")
print("GAME OVER")