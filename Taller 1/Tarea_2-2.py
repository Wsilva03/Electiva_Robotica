<<<<<<< HEAD
import random

cantidad = int(input("Ingrese la cantidad de numeros deseada: \n"))
a = int(input("Ingrese el rango de numeros:\nIniciar en:\n"))
b = int(input("Finalizar en:\n"))
if b>a:
    print("Los numeros generados son:")

    for i in range(cantidad):
        numero_generado = random.randint(a, b)
        print(numero_generado)

else:
    print("***Los valores ingresados no son correctos***\n")
    
=======
import random

cantidad = int(input("Ingrese la cantidad de numeros deseada: \n"))
a = int(input("Ingrese el rango de numeros:\nIniciar en:\n"))
b = int(input("Finalizar en:\n"))
if b>a:
    print("Los numeros generados son:")

    for i in range(cantidad):
        numero_generado = random.randint(a, b)
        print(numero_generado)

else:
    print("***Los valores ingresados no son correctos***\n")
    
>>>>>>> 93bd2c0f80925fbafb79295064af358832d2eac4
print("\n***Programa terminado***\n")