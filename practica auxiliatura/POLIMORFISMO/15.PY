class Ordenador:
    def __init__(self, serial: str, numero: int, ram: int, procesador: str, estado: str):
        self.serial = serial
        self.numero = numero
        self.ram = ram
        self.procesador = procesador
        self.estado = estado 
        
    def mostrarDatos(self):
        return f"Serial: {self.serial:<8} | Numero: {self.numero:<2} | RAM: {self.ram:<2} GB | Procesador: {self.procesador:<10} | Estado: {self.estado}"

    def esActivo(self) -> bool:
        return self.estado.lower() == "activo"

class Laboratorio:
    def __init__(self, nombre: str, capacidad: int):
        self.nombre = nombre
        self.capacidad = capacidad
        self.ordenadores = []
        self.nroOrdenadores = 0

    def adicionar(self, ordenador: Ordenador):
        if self.nroOrdenadores < self.capacidad:
            self.ordenadores.append(ordenador)
            self.nroOrdenadores += 1
        else:
            print(f"ERROR: Laboratorio {self.nombre} lleno. Capacidad {self.capacidad}.")

    def remover(self, serial: str) -> Ordenador:
        for i, ord in enumerate(self.ordenadores):
            if ord.serial == serial:
                ordenador_removido = self.ordenadores.pop(i)
                self.nroOrdenadores -= 1
                return ordenador_removido
        return None

    def informacion(self, parametro=None):
        print(f"\n--- INFORME LABORATORIO {self.nombre} ---")
        
        if parametro is None:

            print("Mostrando TODOS los ordenadores:")
            for ord in self.ordenadores:
                print(f"- {ord.mostrarDatos()}")
        
        elif isinstance(parametro, str):

            estado_buscado = parametro.lower()
            print(f"Mostrando ordenadores con ESTADO '{estado_buscado}':")
            encontrados = 0
            for ord in self.ordenadores:
                if ord.estado.lower() == estado_buscado:
                    print(f"- {ord.mostrarDatos()}")
                    encontrados += 1
            if encontrados == 0:
                print("  (No se encontraron ordenadores con ese estado)")
        
        elif isinstance(parametro, int):

            ram_minima = parametro
            print(f"Mostrando ordenadores con RAM mayor a {ram_minima} GB:")
            encontrados = 0
            for ord in self.ordenadores:
                if ord.ram > ram_minima:
                    print(f"- {ord.mostrarDatos()}")
                    encontrados += 1
            if encontrados == 0:
                print("  (No se encontraron ordenadores con RAM superior)")
        
        else:
            print("ERROR: Parametro de informacion no reconocido.")

def trasladarOrdenadores(lab_origen: Laboratorio, lab_destino: Laboratorio, serial1: str, serial2: str):
    print(f"\n===== INICIO TRASLADO: {lab_origen.nombre} a {lab_destino.nombre} =====")
    
    print("\n ESTADO ANTES DEL TRASLADO ")
    lab_origen.informacion()
    lab_destino.informacion()

    ordenador1 = lab_origen.remover(serial1)
    ordenador2 = lab_origen.remover(serial2)

    if ordenador1:
        lab_destino.adicionar(ordenador1)
        print(f"Trasladado: {serial1}")
    if ordenador2:
        lab_destino.adicionar(ordenador2)
        print(f"Trasladado: {serial2}")
        
    print("\n--- ESTADO DESPUES DEL TRASLADO ---")
    lab_origen.informacion()
    lab_destino.informacion()
    print("=================================================================")

o1 = Ordenador("S001", 1, 4, "i3-10th", "inactivo")
o2 = Ordenador("S002", 2, 8, "i5-11th", "activo")
o3 = Ordenador("S003", 3, 16, "i7-12th", "activo")
o4 = Ordenador("S004", 4, 16, "Ryzen 5", "activo")
o5 = Ordenador("S005", 5, 8, "Ryzen 7", "inactivo")
o6 = Ordenador("S006", 6, 4, "i3-7th", "inactivo")

lab1 = Laboratorio("Lasin 1", 5)
lab2 = Laboratorio("Lasin 2", 5)

lab1.adicionar(o1)
lab1.adicionar(o2)
lab1.adicionar(o3)
lab1.adicionar(o6)

lab2.adicionar(o4)
lab2.adicionar(o5)

print("\n\n B) DEMOSTRACION DE METODO INFORMACION (POLIMORFISMO)")

lab1.informacion()

lab1.informacion("activo")

lab2.informacion(8)

trasladarOrdenadores(lab1, lab2, "S003", "S006")