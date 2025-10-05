class Videojuego:
    def __init__(self, nombre: str, plataforma: str = None, cant_jugadores: int = 0):
        self.nombre = nombre
        self.plataforma = plataforma
        self.cant_jugadores = cant_jugadores
        print(f"Videojuego '{self.nombre}' creado.")

    def agregarJugadores(self, cantidad_o_nada=None):
        if cantidad_o_nada is None:
            self.cant_jugadores += 1
            print(f"[{self.nombre}] Jugador agregado. Total: {self.cant_jugadores} ahora.")
        elif isinstance(cantidad_o_nada, int):
            self.cant_jugadores += cantidad_o_nada
            print(f"[{self.nombre}] Se agregaron {cantidad_o_nada} jugadores. Total: {self.cant_jugadores} ahora.")
        else:
            print("ERROR: Cantidad de jugadores no valida.")

    def reportarJugadores(self) -> int:
        return self.cant_jugadores

v1 = Videojuego("Tierra de Calculo")        
v2 = Videojuego("Programacion Hero", "PC", 2) 

print("\n--- DEMOSTRACION DEL METODO SOBRECARGADO (POLIMORFISMO) ---")

print("-> Llamada 1: Un jugador a la vez")
v1.agregarJugadores() 
v2.agregarJugadores()

print("\n-> Llamada 2: Varios jugadores (INGRESO POR TECLADO)")

cantidad_input = input(f"Ingrese cuantos jugadores desea agregar a {v1.nombre}: ")
cantidad = int(cantidad_input)
v1.agregarJugadores(cantidad)

v2.agregarJugadores(5)

print("\n--- ESTADO FINAL (Usando el metodo reportarJugadores) ---")
print(f"Estado Final de {v1.nombre}: {v1.reportarJugadores()} jugadores.")
print(f"Estado Final de {v2.nombre}: {v2.reportarJugadores()} jugadores.")