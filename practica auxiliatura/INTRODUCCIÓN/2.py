class Bus:
    COSTO_PASAJE = 1.50

    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.pasajeros = 0  
        self.recaudacion = 0.0

    def subir(self, cantidad: int):
        espacio = self.capacidad - self.pasajeros
        
        if cantidad <= espacio:
            self.pasajeros += cantidad
            print(f"Suben {cantidad} pasajeros. Bus: {self.pasajeros}/{self.capacidad}")
            return cantidad
        else:
            pax_suben = espacio
            self.pasajeros += pax_suben
            print(f"Suben {pax_suben} pasajeros. El Bus esta lleno")
            return pax_suben

    def cobrar(self, cantidad_pax: int):
        monto = cantidad_pax * Bus.COSTO_PASAJE
        self.recaudacion += monto
        print(f"Se cobro Bs. {monto:.2f} a {cantidad_pax} personas. Recaudacion total: Bs. {self.recaudacion:.2f}")

    def asientos_libres(self) -> int:
        return self.capacidad - self.pasajeros

mibus = Bus(20)

print(f"Simulacion Bus UMSA")

print("\nParada 1")
pax_p1 = 12
subieron = mibus.subir(pax_p1)
mibus.cobrar(subieron)

print(f"Asientos libres restantes: {mibus.asientos_libres()}") 

print("\nParada 2")
pax_p2 = 10
subieron = mibus.subir(pax_p2)
mibus.cobrar(subieron)

print(f"Asientos libres restantes: {mibus.asientos_libres()}") 

print(f"\nREPORTE FINAL: Pasajeros: {mibus.pasajeros} | Recaudacion: Bs. {mibus.recaudacion:.2f}")