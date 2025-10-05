class Politico:
    def __init__(self, profesion: str, anosExp: int):
        self.profesion = profesion
        self.anosExp = anosExp
    
    def obtener_profesion(self):
        return self.profesion

class Partido:
    def __init__(self, nombreP: str, rol: str):
        self.nombreP = nombreP
        self.rol = rol 
    
    def obtener_nombre_partido(self):
        return self.nombreP

class Presidente(Politico, Partido):
    def __init__(self, nombre: str, apellido: str, profesion: str, anosExp: int, nombreP: str, rol: str):
        self.nombre = nombre
        self.apellido = apellido

        Politico.__init__(self, profesion, anosExp)
        Partido.__init__(self, nombreP, rol)

    def mostrar_info_completa(self):
        print(f"Presidente: {self.nombre} {self.apellido}")
        print(f"Profesion: {self.obtener_profesion()} | Experiencia: {self.anosExp} anios")
        print(f"Partido: {self.obtener_nombre_partido()} ({self.rol})")

def buscar_presidente(vector_presidentes: list[Presidente], nombre_buscado: str):
    print(f"\n--- BUSCANDO PRESIDENTE CON NOMBRE '{nombre_buscado}' ---")
    for p in vector_presidentes:
        if p.nombre.lower() == nombre_buscado.lower():
            print(f"Presidente Encontrado: {p.nombre} {p.apellido}")
            print(f"Partido Politico: {p.obtener_nombre_partido()}")
            print(f"Profesion: {p.obtener_profesion()}")
            return
    print(f"ERROR: Presidente con nombre '{nombre_buscado}' no encontrado.")

p1 = Presidente("Carlos", "Mesa", "Historiador", 30, "FRI", "Opositor")

datos_personales = {"nombre": "Evo", "apellido": "Morales"}
datos_politico = {"profesion": "Sindicalista", "anosExp": 25}
datos_partido = {"nombreP": "MAS", "rol": "Gobernante"}

p2 = Presidente(
    datos_personales["nombre"], datos_personales["apellido"],
    datos_politico["profesion"], datos_politico["anosExp"],
    datos_partido["nombreP"], datos_partido["rol"]
)

p3 = Presidente("Jeanine", "Anez", "Abogada", 15, "UD", "Transicion")


print("--- INFORMACION DE INSTANCIAS ---")
p1.mostrar_info_completa()
print("-" * 30)
p2.mostrar_info_completa()
print("-" * 30)

vector_presidentes = [p1, p2, p3]

buscar_presidente(vector_presidentes, "Evo")
buscar_presidente(vector_presidentes, "Carlos")
buscar_presidente(vector_presidentes, "Alvaro")