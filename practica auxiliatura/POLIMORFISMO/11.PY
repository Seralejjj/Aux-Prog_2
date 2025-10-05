class Pasajero:
    def __init__(self, nombre: str, edad: int, genero: str):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    
    def __pos__(self):
        print("\n LEYENDO DATOS DEL PASAJERO (++)")
        self.nombre = input("Ingrese nombre del pasajero: ")
        try:
            self.edad = int(input("Ingrese edad: "))
        except ValueError:
            self.edad = 0
        self.genero = input("Ingrese genero (H/M): ")
        return self

    def __neg__(self):
        print("\n MOSTRANDO DATOS DEL PASAJERO (--)")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        return self

class Crucero:
    def __init__(self, nombre: str, paisOrigen: str, paisDestino: str, pasajeros_data: list = None):
        self.nombre = nombre
        self.paisOrigen = paisOrigen
        self.paisDestino = paisDestino
        self.pasajeros = pasajeros_data if pasajeros_data is not None else [[], [], []]
        
        self.nroPasajeros = len(self.pasajeros[0])

    def adicionarPasajero(self, nombre: str, nroHabitacion: int, costoPasaje: float):
        self.pasajeros[0].append(nombre)
        self.pasajeros[1].append(nroHabitacion)
        self.pasajeros[2].append(costoPasaje)
        self.nroPasajeros = len(self.pasajeros[0])
        print(f"Pasajero {nombre} agregado a {self.nombre}.")

    def __pos__(self):
        print(f"\n LEYENDO DATOS DEL CRUCERO {self.nombre} (++)")
        self.paisOrigen = input("Ingrese nuevo Pais de Origen: ")
        self.paisDestino = input("Ingrese nuevo Pais de Destino: ")
        return self

    def __neg__(self):
        print(f"\n MOSTRANDO DATOS DEL CRUCERO {self.nombre} (--)")
        print(f"Origen: {self.paisOrigen} | Destino: {self.paisDestino}")
        print(f"Total Pasajeros: {self.nroPasajeros}")
        print(f"Pasajes: {self.pasajeros[2]}")
        return self

    def __eq__(self, other):
        suma_costo = sum(self.pasajeros[2])
        print(f"\n SUMA TOTAL DE PASAJES DE {self.nombre} (==) ")
        print(f"Costo Total: Bs. {suma_costo:.2f}")
        return suma_costo

    def __add__(self, other):
        print("\n COMPARACION DE CANTIDAD DE PASAJEROS (+) ")
        if self.nroPasajeros == other.nroPasajeros:
            resultado = True
            print(f"Resultado: TRUE. Ambos cruceros tienen {self.nroPasajeros} pasajeros.")
        else:
            resultado = False
            print(f"Resultado: FALSE. {self.nombre}: {self.nroPasajeros} vs {other.nombre}: {other.nroPasajeros}.")
        return resultado

    def __sub__(self, lista_pasajeros_objetos):
        hombres = 0
        mujeres = 0
        for pasajero in lista_pasajeros_objetos:
            if pasajero.genero.upper() == 'H':
                hombres += 1
            elif pasajero.genero.upper() == 'M':
                mujeres += 1
        
        print(f"\n REPORTE DE GENERO PARA CRUCERO {self.nombre} (-)")
        print(f"Hombres: {hombres} | Mujeres: {mujeres}")
        return {"hombres": hombres, "mujeres": mujeres}
    
c1_data = [
    ["Juan", "Martina"],  
    [502, 603],           
    [500.0, 1000.0]       
]
c2_data = [
    ["Wilmer", "Andrea", "Pablo"], 
    [401, 707, 303],
    [925.0, 600.0, 750.0]
]

C1 = Crucero("El Titanic II", "Bolivia", "Panama", c1_data)
C2 = Crucero("El Poseidon", "Peru", "Chile", c2_data)

p1 = Pasajero("Juan", 30, "H")
p2 = Pasajero("Martina", 25, "M")
p3 = Pasajero("Wilmer", 45, "H")
p4 = Pasajero("Andrea", 22, "M")
p5 = Pasajero("Pablo", 50, "H")
lista_pasajeros_c2 = [p3, p4, p5]

print("\n B) SOBRECARGA ++ Y -- EN CRUCERO")
+C1
-C1 

print("\n B) SOBRECARGA ++ Y -- EN PASAJERO")
+p1 
-p1 

print("\n C) SOBRECARGA == (SUMA PASAJES)")
C1 == C2 

print("\n D) SOBRECARGA + (COMPARACION DE CANTIDAD DE PASAJEROS)")
C1 + C2 

print("\n E) SOBRECARGA - (CONTEO DE GENERO)")
C2 - lista_pasajeros_c2 