class Producto:
    def __init__(self, nombre: str, precio: float, stock_inicial: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial
    
    def vender(self, cantidad: int):
        if cantidad <= self.stock:
            self.stock -= cantidad
            ingreso = cantidad * self.precio
            print(f"VENTA: Se vendieron {cantidad} de {self.nombre}. Ingreso: Bs. {ingreso:.2f}")
        else:
            print(f"ERROR: No hay suficiente stock para vender {cantidad} de {self.nombre}. Stock actual: {self.stock}")

    def reabastecer(self, cantidad: int):
        self.stock += cantidad
        print(f"REABASTECIMIENTO: Se agregaron {cantidad} unidades de {self.nombre}.")

    def obtener_stock(self) -> int:
        return self.stock
    
cuaderno = Producto("Cuaderno Universitario", 15.00, 80)

print("ESTADO INICIAL")
print(f"Stock de {cuaderno.nombre}: {cuaderno.obtener_stock()}")

print("\nOPERACION VENTA EXITOSA ")
cuaderno.vender(30)
print(f"Nuevo Stock: {cuaderno.obtener_stock()}")

print("\nOPERACION REABASTECER ")
cuaderno.reabastecer(50)
print(f"Nuevo Stock: {cuaderno.obtener_stock()}")

print("\nOPERACION VENTA FALLIDA ")
cuaderno.vender(150)
print(f"Stock Final: {cuaderno.obtener_stock()}")