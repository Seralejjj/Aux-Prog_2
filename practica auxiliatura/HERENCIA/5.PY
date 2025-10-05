class Vehiculo:
    def __init__(self, conductor: str, placa: str, id: int):
        self.conductor = conductor
        self.placa = placa
        self.id = id

    def mostrar_placa_conductor(self):
        print(f"Tipo: {self.__class__.__name__:<8} | Placa: {self.placa:<8} | Conductor: {self.conductor}")

    def cambiar_conductor(self, nuevo_conductor: str):
        print(f"[{self.placa}] Cambiando conductor: {self.conductor} -> {nuevo_conductor}")
        self.conductor = nuevo_conductor
    
    def mostrar_datos(self):
        datos = f"ID: {self.id} | Placa: {self.placa} | Conductor: {self.conductor}"
        return datos

class Bus(Vehiculo):
    def __init__(self, conductor: str, placa: str, id: int, capacidad: int, sindicato: str):
        super().__init__(conductor, placa, id)
        self.capacidad = capacidad
        self.sindicato = sindicato
    
    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        return f"{datos_base} | Capacidad: {self.capacidad} | Sindicato: {self.sindicato}"

class Auto(Vehiculo):
    def __init__(self, conductor: str, placa: str, id: int, caballosFuerza: int, descapotable: bool):
        super().__init__(conductor, placa, id)
        self.caballosFuerza = caballosFuerza
        self.descapotable = descapotable
    
    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        desc = "SI" if self.descapotable else "NO"
        return f"{datos_base} | HP: {self.caballosFuerza} | Descapotable: {desc}"

class Moto(Vehiculo):
    def __init__(self, conductor: str, placa: str, id: int, cilindrada: int, casco: bool):
        super().__init__(conductor, placa, id)
        self.cilindrada = cilindrada
        self.casco = casco
    
    def mostrar_datos(self):
        datos_base = super().mostrar_datos()
        cs = "SI" if self.casco else "NO"
        return f"{datos_base} | Cilindrada: {self.cilindrada} cc | Casco Incluido: {cs}"

print(" DEMOSTRACION DE HERENCIA Y METODOS ")


v_bus = Bus("Raul Choque", "ABC-123", 101, 40, "Trans UMSA")
v_auto = Auto("Ana Perez", "XYZ-456", 202, 180, True)
v_moto = Moto("Luis Vargas", "MNO-789", 303, 250, False)

arreglo_vehiculos = [v_bus, v_auto, v_moto]

print("\n B) PLACA Y CONDUCTOR")
for v in arreglo_vehiculos:
    v.mostrar_placa_conductor()

print("\n DATOS COMPLETOS ANTES DEL CAMBIO ")
for v in arreglo_vehiculos:
    print(v.mostrar_datos())

print("\n C) CAMBIAR CONDUCTOR ")
v_bus.cambiar_conductor("Maria Choque")
v_auto.cambiar_conductor("Juan Caceres")

print("\n DATOS COMPLETOS DESPUES DEL CAMBIO ")
for v in arreglo_vehiculos:
    print(v.mostrar_datos())