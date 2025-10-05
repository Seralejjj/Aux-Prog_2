class Fruta:
    def __init__(self, nombre: str, tipo: str, vitaminas_lista: list):
        self.nombre = nombre
        self.tipo = tipo
        self.vitaminas = vitaminas_lista
        self.nroVitaminas = len(vitaminas_lista)
    
    def mostrar_vitaminas(self):
        vits = ", ".join(self.vitaminas)
        print(f"[{self.nombre}] Vitaminas: {vits}")
    
    def es_citrica(self):
        vitaminas_citricas = ["C"]
        for vit in self.vitaminas:
            if vit in vitaminas_citricas:
                return True
        return False
    
    def obtener_vitaminas_ordenadas(self):
        return sorted(self.vitaminas)

    def mostrar_datos(self):
        return f"{self.nombre} ({self.tipo}) | Vitaminas: {self.nroVitaminas}"

f1 = Fruta("kiwi", "subtropical", ["K", "C", "E"])

vitaminas_manzana = ["A", "C", "B6"]
f2 = Fruta("manzana", "templada", vitaminas_manzana)

vits_naranja = []
vits_naranja.append("C")
vits_naranja.append("B1")
f3 = Fruta("naranja", "citrica", vits_naranja)

print("FRUTAS INSTANCIADAS")
f1.mostrar_datos()
f2.mostrar_datos()
f3.mostrar_datos()

print("\nB) FRUTA CON MAS VITAMINAS")
frutas = [f1, f2, f3]
mas_vitaminas = frutas[0]
for fruta in frutas:
    if fruta.nroVitaminas > mas_vitaminas.nroVitaminas:
        mas_vitaminas = fruta
        
print(f"La fruta con mas vitaminas es {mas_vitaminas.nombre} con {mas_vitaminas.nroVitaminas} vitaminas.")

print("\nC) VITAMINAS DE LA FRUTA X (NARANJA)")
fruta_x = f3
fruta_x.mostrar_vitaminas()

print("\nD) CUANTAS FRUTAS SON CITRICAS (Contienen Vitamina C)")
citas_citricas = 0
for fruta in frutas:
    if fruta.es_citrica():
        citas_citricas += 1

print(f"Numero de frutas que contienen Vitamina C: {citas_citricas}")


print("\nE) FRUTAS ORDENADAS POR VITAMINAS")

frutas_ordenadas = sorted(frutas, key=lambda f: f.obtener_vitaminas_ordenadas())

print("Orden Alfabetico (por vitamina principal, ej: 'A' vs 'C' vs 'K'):")
for fruta in frutas_ordenadas:
    vits_ord = ", ".join(fruta.obtener_vitaminas_ordenadas())
    print(f"- {fruta.nombre} Vitaminas Ordenadas: {vits_ord}")