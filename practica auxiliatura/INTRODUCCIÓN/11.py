class Pedido:
    def __init__(self, estado: str, num_productos: int):
        self._estado = estado
        self._num_productos = num_productos
        print(f"Pedido creado. Estado inicial: {self._estado}")

    def get_estado(self):
        return self._estado
    
    def get_num_productos(self):
        return self._num_productos

    def set_estado(self, nuevo_estado: str):
        self._estado = nuevo_estado
        print(f"Estado del Pedido actualizado a: {self._estado}")

    def mostrar_datos(self):
        print(f"Tipo de objeto: PEDIDO | Estado: {self.get_estado()} | Items: {self.get_num_productos()}")


class Producto:
    def __init__(self, nombre: str, precio: float):
        self._nombre = nombre
        self._precio = precio
        print(f"Producto '{self._nombre}' cargado en el menu.")

    def get_nombre(self):
        return self._nombre
    
    def get_precio(self):
        return self._precio

    def set_nombre(self, nuevo_nombre: str):
        self._nombre = nuevo_nombre
    
    def set_precio(self, nuevo_precio: float):
        self._precio = nuevo_precio

    def mostrar_datos(self):
        print(f"Tipo de objeto: PRODUCTO | Nombre: {self.get_nombre()} | Precio: Bs. {self.get_precio():.2f}")

print("\nCREACION DE OBJETOS")
p = Producto("Te de Coca", 5.00)
ped = Pedido("registrado", 2)

print("\nDATOS DE LOS OBJETOS")
p.mostrar_datos()
ped.mostrar_datos()

# Demostración de Setter/Getter
print("\nDEMOSTRACION DE METODOS")
ped.set_estado("entregado")
print(f"Verificando estado con Getter: {ped.get_estado()}")