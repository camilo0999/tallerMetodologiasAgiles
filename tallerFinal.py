#TALLER 3 SALA DE CINE

# INTERANTES 

#JUAN CAMILO IBARGUEN
#DANIEL MATEO TORRES
#VALERIA PALOMA
#ALAN SALAZAR

#ANTES DE EJECUTAR POR FAVOR CREE UN ARCHIVO UN ARCHIVO "sala.txt" ANTES DE EJECUTAR EL CODIGO PARA QUE PUEDA GUARDAR LOS DATOS DE LA SALA SIN PROBLEMA.

import os
sala = []

def crear_sala():
    global sala
    try:
        filas = int(input("Introduce el número de filas: "))
        columnas = int(input("Introduce el número de columnas: "))
        
        if filas <= 0 or columnas <= 0:
            print("El número de filas y columnas debe ser mayor que 0.")
            return
        
        sala = []
        puesto = 1
        
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(puesto)
                puesto += 1
            sala.append(fila)
        
        print("\nSala creada:")
        for fila in sala:
            print("\t".join(map(str, fila)))
    
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

def ver_sala():
    global sala
    if not sala:
        print("No hay ninguna sala creada. Por favor, crea una sala primero.")
        return
    
    print("\nSala actual:")
    for fila in sala:
        print("\t".join(map(str, fila)))

def asignar_puesto():
    global sala
    if not sala:
        print("No hay ninguna sala creada. Por favor, crea una sala primero.")
        return
    
    print("\nDisponibilidad actual de los puestos:")
    ver_sala() 
    
    try:
        puesto_asignar = int(input("Introduce el número del puesto a asignar: "))
        asignado = False
        
        for i in range(len(sala)):
            for j in range(len(sala[i])):
                if sala[i][j] == puesto_asignar:
                    sala[i][j] = "X"
                    asignado = True
                    break
            if asignado:
                break
        
        if asignado:
            print(f"Puesto {puesto_asignar} asignado con éxito.")
        else:
            print(f"Puesto {puesto_asignar} no encontrado o ya asignado.")
        
        ver_sala()  
    
    except ValueError:
        print("Entrada no válida. Por favor, introduce un número.")

def guardar_sala():
    global sala
    try:
        with open("sala.txt", "w") as archivo:
            for fila in sala:
                archivo.write("\t".join(map(str, fila)) + "\n")
        print("Sala guardada en 'sala.txt'.")
    except IOError:
        print("Error al guardar la sala en el archivo.")

def cargar_sala_desde_archivo():
    global sala
    if not os.path.exists("sala.txt"):
        print("No se encontró el archivo 'sala.txt'. Por favor, guarda una sala primero.")
        return
    
    try:
        with open("sala.txt", "r") as archivo:
            sala = []
            for linea in archivo:
                fila = linea.strip().split("\t")
                fila = ["X" if item == "X" else int(item) for item in fila]
                sala.append(fila)
        print("Sala cargada desde 'sala.txt'.")
        ver_sala()
    except IOError:
        print("Error al cargar la sala desde el archivo.")

def salir():
    guardar_sala()  
    print("Saliendo del programa.")
    exit()

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. CREAR SALA")
    print("2. VER SALA")
    print("3. ASIGNAR PUESTO")
    print("4. CARGAR SALA DESDE ARCHIVO")
    print("5. SALIR")

def ejecutar_opcion(opcion):
    if opcion == 1:
        crear_sala()
    elif opcion == 2:
        ver_sala()
    elif opcion == 3:
        asignar_puesto()
    elif opcion == 4:
        cargar_sala_desde_archivo()
    elif opcion == 5:
        salir()
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")

def main():
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Selecciona una opción: "))
            ejecutar_opcion(opcion)
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")

if __name__ == "__main__":
    main()
