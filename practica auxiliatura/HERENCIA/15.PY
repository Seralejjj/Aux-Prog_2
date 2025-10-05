class Nadador:
    def __init__(self, estiloNatacion: str):
        self.estiloNatacion = estiloNatacion
    
    def nadar(self):
        print(f"Nadando estilo {self.estiloNatacion}.")

class Ciclista:
    def __init__(self, tipoBicicleta: str):
        self.tipoBicicleta = tipoBicicleta
    
    def pedalear(self):
        print(f"Pedaleando en bicicleta tipo {self.tipoBicicleta}.")

class Corredor:
    def __init__(self, distanciaPreferida: float):
        self.distanciaPreferida = distanciaPreferida
    
    def correr(self):
        print(f"Corriendo una distancia de {self.distanciaPreferida} km.")

class Triatleta(Nadador, Ciclista, Corredor):
    def __init__(self, estiloNatacion: str, tipoBicicleta: str, distanciaPreferida: float, nombre: str):
        self.nombre = nombre
        
        Nadador.__init__(self, estiloNatacion)
        Ciclista.__init__(self, tipoBicicleta)
        Corredor.__init__(self, distanciaPreferida)

triatleta1 = Triatleta(
    estiloNatacion="Libre", 
    tipoBicicleta="Ruta", 
    distanciaPreferida=21.09,
    nombre="Daniela"
)

print(f"--- ACCIONES DEL TRIATLETA: {triatleta1.nombre} ---")

print("\nParte 1: Natacion (Heredado de Nadador)")
triatleta1.nadar()

print("\nParte 2: Ciclismo (Heredado de Ciclista)")
triatleta1.pedalear()

print("\nParte 3: Carrera (Heredado de Corredor)")
triatleta1.correr()