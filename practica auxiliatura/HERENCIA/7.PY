class Persona:
    def __init__(self, nombre: str, paterno: str, materno: str, edad: int):

        self._nombre = nombre
        self._paterno = paterno
        self._materno = materno
        self._edad = edad
    
    def mostrar(self):
        nombre_completo = f"{self._nombre} {self._paterno} {self._materno}"
        print(f"Nombre: {nombre_completo:<30} | Edad: {self._edad}")
        return self._edad 

class Docente(Persona):
    def __init__(self, nombre: str, paterno: str, materno: str, edad: int, sueldo: int, regProfesional: str):
        super().__init__(nombre, paterno, materno, edad)
        self._sueldo = sueldo
        self._regProfesional = regProfesional

    def mostrar(self):
        print("\n--- DATOS DOCENTE ---")
        edad_docente = super().mostrar() 
        print(f"Sueldo: Bs. {self._sueldo} | Reg. Prof.: {self._regProfesional}")
        return edad_docente

class Estudiante(Persona):
    def __init__(self, nombre: str, paterno: str, materno: str, edad: int, ru: str, matricula: str):
        super().__init__(nombre, paterno, materno, edad)

        self._ru = ru
        self._matricula = matricula

    def mostrar(self):
        print("--- DATOS ESTUDIANTE ---")
        edad_estudiante = super().mostrar() 
        print(f"RU: {self._ru} | Matricula: {self._matricula}")
        return edad_estudiante

    def modificarEdad(self, nueva_edad: int):
        if nueva_edad > 0 and nueva_edad != self._edad:
            print(f"Modificando edad de {self._nombre}: {self._edad} -> {nueva_edad}")
            self._edad = nueva_edad
        else:
            print("ERROR: Edad no valida o sin cambios.")

def promedio_edad_estudiantes(lista_estudiantes: list[Estudiante]):
    if not lista_estudiantes:
        return 0
    suma_edades = sum(estudiante._edad for estudiante in lista_estudiantes)
    promedio = suma_edades / len(lista_estudiantes)
    return promedio

e1 = Estudiante("Juan", "Vargas", "Montero", 20, "123-UMSA", "A-2023")
e2 = Estudiante("Maria", "Perez", "Lopez", 22, "456-UMSA", "B-2022")
d1 = Docente("Wilmer", "Guzman", "Mamani", 45, 8000, "RP-001")

lista_estudiantes = [e1, e2]

print("--- B) MOSTRAR DATOS ---")
edad_e1 = e1.mostrar()
edad_e2 = e2.mostrar()
edad_d1 = d1.mostrar()

print("\n--- C) PROMEDIO DE EDADES ---")
promedio = promedio_edad_estudiantes(lista_estudiantes)
print(f"El promedio de edad de los estudiantes es: {promedio:.2f} anios.")

print("\n--- D) MODIFICAR EDAD ---")
e1.modificarEdad(21)
e1.mostrar()

print("\n--- E) VERIFICAR MISMA EDAD ---")
# Usamos la edad modificada de e1 (21)
edad_e1_final = e1._edad
print(f"Edad Estudiante 1 (final): {edad_e1_final} | Edad Docente: {edad_d1}")

if edad_e1_final == edad_d1:
    print(f"El estudiante {e1._nombre} tiene la misma edad que el docente.")
elif edad_e2._edad == edad_d1:
    print(f"El estudiante {e2._nombre} tiene la misma edad que el docente.")
else:
    print("Ningun estudiante tiene la misma edad que el docente.")