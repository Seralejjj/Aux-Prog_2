class Persona:
    def __init__(self, nombre: str, paterno: str, materno: str, edad: int, ci: str):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno
        self.edad = edad
        self.ci = ci
    
    def mostrarDatos(self):
        print(f"Nombre: {self.nombre} {self.paterno} {self.materno}")
        print(f"Edad: {self.edad} años | CI: {self.ci}")
    
    def mayorDeEdad(self) -> bool:
        return self.edad >= 18
    
    def modificarEdad(self, nueva_edad: int):
        if nueva_edad > 0:
            self.edad = nueva_edad
            print(f"La edad de {self.nombre} ha sido modificada a {self.edad} años.")
        else:
            print("ERROR: La edad debe ser un numero positivo.")

p1 = Persona("Ana", "Mamani", "Flores", 25, "10123456")
p2 = Persona("Luis", "Mamani", "Vargas", 17, "20987654")


print("DATOS INICIALES")
print("\n[Persona 1]")
p1.mostrarDatos() 
print(f"Es mayor de edad: {p1.mayorDeEdad()}") # c

print("\n[Persona 2]")
p2.mostrarDatos() 
print(f"Es mayor de edad: {p2.mayorDeEdad()}") # c

print("\nMODIFICACIÓN DE EDAD")
p2.modificarEdad(19)
print(f"Nueva edad de {p2.nombre}: {p2.edad}")

print("\nVERIFICACIÓN DE APELLIDO")

if p1.paterno == p2.paterno:
    print(f"Resultado: Verdadero Ambas personas son de la familia {p1.paterno}.")
else:
    print(f"Resultado: Falso Los apellidos paternos son diferentes ({p1.paterno} vs {p2.paterno}).")