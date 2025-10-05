class Animal:
    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        self.edad = edad

    def desplazarse(self):
        print(f"{self.nombre} se desplaza de forma generica.")

class Leon(Animal):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"El {self.nombre} (Leon) esta caminando o corriendo.")

class Pinguino(Animal):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"El {self.nombre} (Pinguino) esta nadando o se desliza en el hielo.")

class Canguro(Animal):
    def __init__(self, nombre: str, edad: int):
        super().__init__(nombre, edad)

    def desplazarse(self):
        print(f"El {self.nombre} (Canguro) esta saltando.")

print("DEMOSTRACION DE POLIMORFISMO POR SOBREESCRITURA ")

arreglo_animales = [
    Leon("Simba", 5),
    Pinguino("Pingu", 2),
    Canguro("Skippy", 7),
    Leon("Nala", 6),
    Animal("Generico", 1)
]

for animal in arreglo_animales:
    animal.desplazarse()