import os

# 1. Definición de la clase principal
class Jugador:
    def __init__(self, nombre, edad, posicion, goles):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.goles = goles

    def mostrar_info(self):
        return f"Nombre: {self.nombre} | Edad: {self.edad} | Posición: {self.posicion} | Goles: {self.goles}"

# 2. Implementación de Herencia: Clase Capitán
class Capitan(Jugador):
    def __init__(self, nombre, edad, posicion, goles, liderazgo):
        # Usamos super() para heredar los atributos de Jugador
        super().__init__(nombre, edad, posicion, goles)
        self.liderazgo = liderazgo

    # Sobrescribir mostrar_info
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} | Nivel de Liderazgo: {self.liderazgo}"

# 3. Gestión de archivos
def guardar_jugadores(lista_jugadores, nombre_archivo="jugadores.txt"):
    try:
        with open(nombre_archivo, "w") as archivo:
            for j in lista_jugadores:
                # Guardamos los datos separados por comas
                tipo = "Capitan" if isinstance(j, Capitan) else "Jugador"
                if tipo == "Capitan":
                    linea = f"{tipo},{j.nombre},{j.edad},{j.posicion},{j.goles},{j.liderazgo}\n"
                else:
                    linea = f"{tipo},{j.nombre},{j.edad},{j.posicion},{j.goles}\n"
                archivo.write(linea)
        print("¡Datos guardados exitosamente!")
    except Exception as e:
        print(f"Error al guardar: {e}")

def cargar_jugadores(nombre_archivo="jugadores.txt"):
    jugadores = []
    if not os.path.exists(nombre_archivo):
        print("El archivo no existe aún.")
        return jugadores

    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                tipo = datos[0]
                if tipo == "Capitan":
                    j = Capitan(datos[1], int(datos[2]), datos[3], int(datos[4]), datos[5])
                else:
                    j = Jugador(datos[1], int(datos[2]), datos[3], int(datos[4]))
                jugadores.append(j)
        return jugadores
    except Exception as e:
        print(f"Error al cargar: {e}")
        return []

# 4. Manejo de excepciones y Menú Principal
def menu():
    lista_jugadores = cargar_jugadores()
    
    while True:
        print("\n--- SISTEMA DE GESTIÓN PYTHON FC ---")
        print("1. Registrar Jugador")
        print("2. Registrar Capitán")
        print("3. Listar Jugadores")
        print("4. Guardar y Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion in ["1", "2"]:
            try:
                nombre = input("Nombre: ")
                # Validación de edad y goles con manejo de excepciones
                edad = int(input("Edad: "))
                if edad < 0: raise ValueError("La edad no puede ser negativa.")
                
                posicion = input("Posición: ")
                
                goles = int(input("Goles: "))
                if goles < 0: raise ValueError("Los goles no pueden ser negativos.")

                if opcion == "1":
                    nuevo_j = Jugador(nombre, edad, posicion, goles)
                else:
                    liderazgo = input("Nivel de liderazgo (Bajo/Medio/Alto): ")
                    nuevo_j = Capitan(nombre, edad, posicion, goles, liderazgo)
                
                lista_jugadores.append(nuevo_j)
                print("¡Registrado con éxito!")

            except ValueError as e:
                print(f"Error de entrada: {e}. Por favor, ingrese números válidos.")

        elif opcion == "3":
            print("\n--- LISTA DE JUGADORES ---")
            if not lista_jugadores:
                print("No hay jugadores registrados.")
            for j in lista_jugadores:
                print(j.mostrar_info())

        elif opcion == "4":
            guardar_jugadores(lista_jugadores)
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()