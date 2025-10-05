class Matriz:
    def __init__(self, tamano: int, valores_iniciales: list = None):
        self.tamano = tamano
        if valores_iniciales is None:

            self.datos = [[1.0 if i == j else 0.0 for j in range(tamano)] for i in range(tamano)]
            print(f"Matriz de identidad de {tamano}x{tamano} creada.")
        else:

            if len(valores_iniciales) == tamano and all(len(fila) == tamano for fila in valores_iniciales):
                self.datos = valores_iniciales
                print(f"Matriz de {tamano}x{tamano} creada con valores dados.")
            else:
                raise ValueError("Los valores iniciales no coinciden con el tamano de la matriz.")

    def sumar(self, otraMatriz):
        if self.tamano != otraMatriz.tamano:
            print("ERROR: Las matrices deben ser del mismo tamano para sumar.")
            return None
        
        nueva_matriz_datos = []
        for i in range(self.tamano):
            fila_nueva = []
            for j in range(self.tamano):
                valor = self.datos[i][j] + otraMatriz.datos[i][j]
                fila_nueva.append(valor)
            nueva_matriz_datos.append(fila_nueva)
            
        return Matriz(self.tamano, nueva_matriz_datos)

    def restar(self, otraMatriz):
        if self.tamano != otraMatriz.tamano:
            print("ERROR: Las matrices deben ser del mismo tamano para restar.")
            return None
        
        nueva_matriz_datos = []
        for i in range(self.tamano):
            fila_nueva = []
            for j in range(self.tamano):
                valor = self.datos[i][j] - otraMatriz.datos[i][j]
                fila_nueva.append(valor)
            nueva_matriz_datos.append(fila_nueva)
            
        return Matriz(self.tamano, nueva_matriz_datos)

    def igual(self, otraMatriz) -> bool:
        if self.tamano != otraMatriz.tamano:
            return False
        
        for i in range(self.tamano):
            for j in range(self.tamano):
                if self.datos[i][j] != otraMatriz.datos[i][j]:
                    return False
        return True

    def mostrar(self):
        for fila in self.datos:
            print(fila)

print("1. SOBRECARGA DE CONSTRUCTOR")

M_identidad = Matriz(3)
M_identidad.mostrar()

valores_A = [[5.0, 2.0], [1.0, 3.0]]
M_a = Matriz(2, valores_A)
M_a.mostrar()

valores_B = [[1.0, 1.0], [0.0, 2.0]]
M_b = Matriz(2, valores_B)
M_b.mostrar()


print("\n2. POLIMORFISMO EN METODOS (Sumar y Restar)")
M_suma = M_a.sumar(M_b)
if M_suma:
    print("Resultado Suma:")
    M_suma.mostrar()

M_resta = M_a.restar(M_b)
if M_resta:
    print("Resultado Resta:")
    M_resta.mostrar()

print("\n3. METODO IGUAL")
M_c = Matriz(2, valores_A)

print(f"M_a es igual a M_b: {M_a.igual(M_b)}")
print(f"M_a es igual a M_c: {M_a.igual(M_c)}")