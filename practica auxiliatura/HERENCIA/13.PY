# CLASE BASE
class Empleado:
    def __init__(self, nombre: str, sueldoMes: float, horasExtra: int):
        self.nombre = nombre
        self.sueldoMes = sueldoMes
        self.horasExtra = horasExtra

    def SueldoTotal(self):
        extra = self.horasExtra * 10
        total = self.sueldoMes + extra
        return total

    def obtenerSueldoMes(self):
        return self.sueldoMes

class Administrativo(Empleado):
    def __init__(self, nombre: str, sueldoMes: float, horasExtra: int):
        super().__init__(nombre, sueldoMes, horasExtra)

    def SueldoTotal(self):
        return super().SueldoTotal()

class Cocinero(Empleado):
    def __init__(self, nombre: str, sueldoMes: float, horasExtra: int, sueldoPorHora: float):
        super().__init__(nombre, sueldoMes, horasExtra)
        self.sueldoPorHora = sueldoPorHora

    def SueldoTotal(self):
        extra = self.horasExtra * self.sueldoPorHora
        total = self.sueldoMes + extra

        return total

class Chef(Cocinero):
    def __init__(self, nombre: str, sueldoMes: float, horasExtra: int, sueldoPorHora: float, especialidad: str):

        super().__init__(nombre, sueldoMes, horasExtra, sueldoPorHora)
        self.especialidad = especialidad
    
    def SueldoTotal(self):
        return super().SueldoTotal()

class Mesero(Empleado):
    def __init__(self, nombre: str, sueldoMes: float, horasExtra: int, propina: float):
        super().__init__(nombre, sueldoMes, horasExtra)
        self.propina = propina

    def SueldoTotal(self):
        extra_generica = self.horasExtra * 10
        total = self.sueldoMes + extra_generica + self.propina

        return total

empleados = [
    Chef("Remy", 7000.0, 10, 50.0, "Francesa"),
    Mesero("Alfredo", 3000.0, 5, 450.0),
    Mesero("Estela", 3000.0, 8, 700.0),
    Administrativo("Gaston", 4500.0, 10),
    Administrativo("Colette", 4500.0, 0)
]

print("--- SUELDO TOTAL (POLIMORFISMO POR SOBREESCRITURA) ---")
for emp in empleados:
    nombre_clase = emp.__class__.__name__
    sueldo_total = emp.SueldoTotal()
    print(f"| {nombre_clase:<15} | {emp.nombre:<10} | Sueldo Total: Bs. {sueldo_total:.2f}")

sueldo_buscado = 4500.0

print(f"\n--- B) EMPLEADOS CON SUELDO MES IGUAL A Bs. {sueldo_buscado:.2f} ---")
encontrados = 0
for emp in empleados:
    if emp.obtenerSueldoMes() == sueldo_buscado:
        print(f"- Encontrado: {emp.nombre} ({emp.__class__.__name__})")
        encontrados += 1
if encontrados == 0:
    print("(No se encontraron empleados con ese sueldo base)")