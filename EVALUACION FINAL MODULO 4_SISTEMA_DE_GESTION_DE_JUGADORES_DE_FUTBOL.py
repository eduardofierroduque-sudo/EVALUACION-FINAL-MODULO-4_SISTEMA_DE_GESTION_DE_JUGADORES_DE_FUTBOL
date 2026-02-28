import os

# 1. Definición de la clase principal
class Jugador:
    def __init__(self, nombre, edad, posicion, goles):
        self.nombre = nombre
        self.edad = edad
        self.posicion = posicion
        self.goles = goles

    def mostrar_info(self):
        # Retornamos la cadena para que sea versátil (imprimir o guardar)
        return f"Nombre: {self.nombre} | Edad: {self.edad} | Posición: {self.posicion} | Goles: {self.goles}"

# 2. Implementación de Herencia: Clase Capitán
class Capitan(Jugador):
    def __init__(self, nombre, edad, posicion, goles, liderazgo):
        # super() conecta con el constructor de Jugador
        super().__init__(nombre, edad, posicion, goles)
        self.liderazgo = liderazgo

    # Sobrescribir mostrar_info (Polimorfismo)
    def mostrar_info(self):
        info_base = super().mostrar_info()
        return f"{info_base} | Nivel de Liderazgo: {self.liderazgo}"

# 3. Gestión de archivos
def guardar_jugadores(lista_jugadores, nombre_archivo="jugadores.txt"):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for j in lista_jugadores:
                tipo = "Capitan" if isinstance(j, Capitan) else "Jugador"
                if tipo == "Capitan":
                    linea = f"{tipo},{j.nombre},{j.edad},{j.posicion},{j.goles},{j.liderazgo}\n"
                else:
                    linea = f"{tipo},{j.nombre},{j.edad},{j.posicion},{j.goles}\n"
                archivo.write(linea)
        print("¡Datos guardados exitosamente en 'jugadores.txt'!")
    except Exception as e:
        print(f"Error crítico al guardar: {e}")

def cargar_jugadores(nombre_archivo="jugadores.txt"):
    jugadores = []
    if not os.path.exists(nombre_archivo):
        return jugadores

    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                # Quitamos espacios y saltos de línea, y saltamos líneas vacías
                contenido = linea.strip()
                if not contenido:
                    continue
                
                datos = contenido.split(",")
                tipo = datos[0]
                
                # Conversión de datos con precaución
                if tipo == "Capitan":
                    # datos[1]=nombre, [2]=edad, [3]=posicion, [4]=goles, [5]=liderazgo
                    j = Capitan(datos[1], int(datos[2]), datos[3], int(datos[4]), datos[5])
                else:
                    j = Jugador(datos[1], int(datos[2]), datos[3], int(datos[4]))
                jugadores.append(j)
        return jugadores
    except (ValueError, IndexError):
        print("Error: El archivo de datos está corrupto o tiene un formato inválido.")
        return []
    except Exception as e:
        print(f"Error inesperado al cargar: {e}")
        return []

# 4. Manejo de excepciones y Menú
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
                nombre = input("Nombre: ").strip()
                if not nombre: raise ValueError("El nombre no puede estar vacío.")
                
                edad = int(input("Edad: "))
                if edad < 0: raise ValueError("La edad no puede ser negativa.")
                
                posicion = input("Posición: ").strip()
                goles = int(input("Goles: "))
                if goles < 0: raise ValueError("La cantidad de goles no puede ser negativa.")

                if opcion == "1":
                    nuevo_j = Jugador(nombre, edad, posicion, goles)
                else:
                    liderazgo = input("Nivel de liderazgo (Bajo/Medio/Alto): ")
                    nuevo_j = Capitan(nombre, edad, posicion, goles, liderazgo)
                
                lista_jugadores.append(nuevo_j)
                print(f"¡{type(nuevo_j).__name__} registrado con éxito!")

            except ValueError as e:
                print(f"Error de entrada: {e}")

        elif opcion == "3":
            print("\n" + "="*40)
            print("LISTA ACTUAL DE JUGADORES")
            print("="*40)
            if not lista_jugadores:
                print("No hay jugadores en la lista.")
            for j in lista_jugadores:
                print(j.mostrar_info())

        elif opcion == "4":
            guardar_jugadores(lista_jugadores)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

if __name__ == "__main__":
    menu()
