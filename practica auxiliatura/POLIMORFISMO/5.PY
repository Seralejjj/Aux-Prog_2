class Celular:
    def __init__(self, nroTel: str, dueno: str, espacio: int, ram: int, nroApp: int):
        self.nroTel = nroTel
        self.dueno = dueno
        self.espacio = espacio
        self.ram = ram
        self.nroApp = nroApp

    def __add__(self, otra_cantidad: int):
        if otra_cantidad == 10:
            self.nroApp += 10
            print(f"Apps aumentadas en 10. Nuevo nroApp: {self.nroApp}")
        return self

    def __sub__(self, otra_cantidad: int):
        if otra_cantidad == 5:
            self.espacio -= 5
            print(f"Espacio disminuido en 5 GB. Nuevo espacio: {self.espacio} GB")
        return self

    def mostrarDatos(self):
        print(f"Dueno: {self.dueno} (Tel: {self.nroTel})")
        print(f"Espacio: {self.espacio} GB | RAM: {self.ram} GB | Apps: {self.nroApp}")

mi_celular = Celular("77712345", "Luis", 64, 8, 35)

print("DATOS INICIALES (d)")
mi_celular.mostrarDatos()

print("\nSOBRECARGA DE OPERADOR (+) (b)")
mi_celular + 10

print("\nSOBRECARGA DE OPERADOR (-) (c)")
mi_celular - 5

print("\nDATOS FINALES (d)")
mi_celular.mostrarDatos()