class persona:
    def __init__(self, nombre: str, apellido: str, ci: str):
        self.nombre = nombre
        self.apellido = apellido
        self.ci = ci
    
    def mostrar_datos(self):
        print(f"CI: {self.ci} | Nombre Completo: {self.nombre} {self.apellido}")

class cliente(persona):
    def __init__(self, nombre: str, apellido: str, ci: str, nroCompra: str, idCliente: str):

        super().__init__(nombre, apellido, ci) 
        self.nroCompra = nroCompra
        self.idCliente = idCliente
        
    def mostrar_datos(self):
        print(" DATOS CLIENTE")

        super().mostrar_datos() 
        print(f"ID Cliente: {self.idCliente} | Ultima Compra: {self.nroCompra}")
        
class jefe(persona):
    def __init__(self, nombre: str, apellido: str, ci: str, sucursal: str, tipo: str):

        super().__init__(nombre, apellido, ci)
        self.sucursal = sucursal
        self.tipo = tipo

    def mostrar_datos(self):
        print(" DATOS JEFE ")

        super().mostrar_datos()
        print(f"Sucursal: {self.sucursal} | Tipo de Jefe: {self.tipo}")

print(" DEMOSTRACION DE HERENCIA CORREGIDA ")

j1 = jefe("Maria", "Perez", "12345", "Zona Central", "Supervisor")
j1.mostrar_datos()

c1 = cliente("Juan", "Vargas", "67890", "F00123", "C-005")
c1.mostrar_datos()