from Funciones.calcpromedio import calcular_promedio
from Funciones.mayor import num_mayor
from Funciones.mostrar import mostrar
from Funciones.impares import impar

lista=[]

while True:
    try:
        num=int(input("Ingrese un número (0 para terminar): "))
        if num==0:
            break
        lista.append(num)
    except ValueError:
        print("Por favor, ingrese un número válido.")

promedio=calcular_promedio(lista)
mayor, menor=num_mayor(lista)
numImpares=impar(lista)

print(mostrar(lista))
print(f"Promedio: {promedio}")
print(f"Mayor: {mayor}, Menor: {menor}")
print(f"Estos son los números impares {numImpares}")
