class Mascota:
    def __init__(self, nombre: str, tipo: str, energia_inicial: int):
        self.nombre = nombre
        self.tipo = tipo
        self.energia = energia_inicial
    
    def alimentar(self):
        self.energia += 20
        if self.energia > 100:
            self.energia = 100
            print(f"[{self.nombre}] se alimento, su energia esta al MAXIMO (100).")
        else:
            print(f"[{self.nombre}] se alimento. Energia actual: {self.energia}")

    def jugar(self):
        self.energia -= 15
        if self.energia < 0:
            self.energia = 0
            print(f"[{self.nombre}] jugo, su energia esta al MINIMO (0). Debe descansar.")
        else:
            print(f"[{self.nombre}] jugo. Energia actual: {self.energia}")

    def mostrar_energia(self):
        print(f"ENERGIA de {self.nombre} ({self.tipo}): {self.energia}")

m1 = Mascota("Bolita", "Perro", 60)
m2 = Mascota("Michi", "Gato", 10)

print("ESTADO INICIAL")
m1.mostrar_energia()
m2.mostrar_energia()

print("\nSIMULACION DE JUEGO Y ALIMENTACION")

print(f"\n[Turno de {m1.nombre}]")
m1.jugar() 
m1.mostrar_energia()
m1.alimentar()
m1.mostrar_energia()

print(f"\n[Turno de {m2.nombre}]")
m2.alimentar()
m2.alimentar()
m2.mostrar_energia()
m2.jugar()
m2.jugar()
m2.jugar() 
m2.jugar()
m2.mostrar_energia()