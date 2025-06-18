# Este código va a servir de introducción y como biblioteca
# para los diferentes codigos que mas adelante utilice.

# Operaciones básicas

# Para valores numéricos tenemos los usuales + suma, - resta, * multiplicación
# / división. Luego poseemos también las operaciones ** potencia, % módulo,
# // división parte entera.

# La suma también funciona como concatenación cuando le entregamos valores
# del tipo string. Y la multiplicación con este tipo de valores funciona como
# repetidor.

# Los strings tambien funcionan como vectores, por lo que de necesitarlo si queremos
# la quinta letra solamente hacemos palabra[5]. Y si queremos un conjunto de ellas
# hacemos palabra[2:5].

# Para los valores complejos se utilizará la letra "j" para el valor complejo.

# Cuando queramos que nos entreguen un valor usaremos "input()". Notemos que esto
# se entrega en formato string, por lo que si solicitamos un dato numérico habrá
# que transformarlo en numérico antes de que entre a las funciones.

# Asignación de variables de distintos tipos
entero = 10
flotante = 3.14
cadena = "Hola, Data Science!"
booleano = True

# Imprimimos cada variable
print("Entero:", entero)
print("Flotante:", flotante)
print("Cadena:", cadena)
print("Booleano:", booleano)

# Podemos usar la función type() para ver el tipo de dato
print("El tipo de 'entero' es:", type(entero))
print("El tipo de 'cadena' es:", type(cadena))

# LISTAS (mutables)
numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)

print("El número de elementos es:", len(numeros)) # Entrega el tamaño de la lista

numeros.append(6)  # Agrega un elemento al final
print("Lista con append:", numeros)

numeros[0] = 10    # Modificamos el primer elemento
print("Lista modificada:", numeros)

# También se pueden modificar varios elementos a la vez usando listas.

valor = numeros.pop(3) # Elimina el elemento en la posición 3, recordar que las posiciones parten del 0.
                       # Si no se coloca un valor, elimina la última posición.
print(numeros)
print(valor)

numeros_cortada = numeros[1:3] # Modifica la lista colocando solamente las posiciones del 1 al 3
numeros_cortada

numeros_cortada = numeros[1:4:2] # Modifica la lista colocando las posiciones del 1 al 4 cada 2
numeros_cortada

# Las listas tambien se pueden concatenar (+) y repetir (*), creando así nuevas listas.

numeros_2 = numeros.copy() # Esto genera una copia de la lista modificables, la cual no afecta a la original.

# TUPLAS (inmutables)
punto = (3, 4)
print("\nTupla:", punto)
# punto[0] = 5  # Esto daría un error, no se pueden modificar las tuplas

# DICCIONARIOS (pares clave-valor)
estudiante = {
    "nombre": "María",
    "edad": 21,
    "carrera": "Ingeniería Matemática"
}
print("\nDiccionario estudiante:", estudiante)
print("Nombre:", estudiante["nombre"])

# Agregamos una nueva clave
estudiante["promedio"] = 5.4
print("Diccionario con nueva clave:", estudiante)

x = 10
if x > 0:
    print("x es positivo")
else:
    print("x es cero o negativo")

animales = ["gato", "perro", "conejo"]
for animal in animales:
    print("El animal es:", animal)

contador = 3
while contador > 0:
    print("Contador:", contador)
    contador -= 1 # Colocar -= o += sirve para asignarle a la variable la operación
                  # directamente, sin necesidad de volver a llamarla. 

def suma(a, b): # Definición de funciones.
    """Función que retorna la suma de a y b."""
    return a + b

resultado = suma(5, 7)
print("La suma de 5 y 7 es:", resultado)

import numpy as np

# Creación de arrays
lista = [1, 2, 3, 4, 5]
arr = np.array(lista)
print("Array de NumPy:", arr)

# Operaciones vectorizadas
print("Suma de 2 a cada elemento:", arr + 2)
print("Producto de elementos por 3:", arr * 3)

# Array aleatorio 3x2
arr_random = np.random.rand(3, 2)
print("\nArray aleatorio de 3x2:\n", arr_random)

# Estadísticas básicas
print("Promedio:", np.mean(arr))
print("Desviación estándar:", np.std(arr))

import pandas as pd

# Crear un DataFrame desde un diccionario
data = {
    "Nombre": ["Ana", "Bernardo", "Claudia"],
    "Edad": [24, 30, 22],
    "Ciudad": ["Bogotá", "México DF", "Lima"]
}

df = pd.DataFrame(data)
print("DataFrame:\n", df)

# Información y primeras filas
print("\nInformación del DataFrame:")
print(df.info())

print("\nPrimeras filas del DataFrame:")
print(df.head())

# Describir datos numéricos
print("\nDescripción estadística:")
print(df.describe())

import matplotlib.pyplot as plt

numeros = [2, 4, 5, 7, 8, 10]
plt.plot(numeros)
plt.title("Ejemplo de Gráfica Sencilla")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.show()