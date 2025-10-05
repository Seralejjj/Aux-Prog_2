class Parada:

    def __init__(self, nombreP: str = "Parada Central", admins_list: list = None, autos_list: list = None):
        self.nombreP = nombreP
        self.admins = admins_list if admins_list is not None else []
        self.autos = autos_list if autos_list is not None else []
        self.nroAdmins = len(self.admins)
        self.nroAutos = len(self.autos)
        print(f"Parada '{self.nombreP}' creada. Autos: {self.nroAutos}, Admins: {self.nroAdmins}")

    def mostrar(self):
        print(f"PARADA: {self.nombreP}")
        
        print("Administradores:")
        if self.nroAdmins == 0:
            print("(No hay administradores)")
        else:
            for admin in self.admins:
                print(f"  - {admin}")
        
        print("\nVehiculos registrados:")
        if self.nroAutos == 0:
            print("  (No hay vehiculos)")
        else:
            print("  Modelo  Conductor  Placa")
            for auto in self.autos:
                print(f"  {auto[0]:<6} | {auto[1]:<9} | {auto[2]}")
        print("-" * (len(self.nombreP) + 15))

    def adicionar(self, x, y=None, z=None):
        if y is None and z is None:

            nombreAdmin = x
            if self.nroAdmins < 10:
                self.admins.append(nombreAdmin)
                self.nroAdmins += 1
                print(f"Admin '{nombreAdmin}' adicionado.")
            else:
                print("ERROR: Limite de admins (10) alcanzado.")

        elif y is not None and z is not None:

            modelo = x
            conductor = y
            placa = z
            if self.nroAutos < 10:
                self.autos.append([modelo, conductor, placa])
                self.nroAutos += 1
                print(f"Auto '{modelo}' (Placa: {placa}) adicionado.")
            else:
                print("ERROR: Limite de autos (10) alcanzado.")
        
        else:
            print("ERROR: Numero de argumentos de adicion no valido.")

parada_defecto = Parada()

admins_inicio = ["Jose"]
autos_inicio = [["Vagoneta", "Raul", "XYZ-123"]]
parada_universidad = Parada("Parada UMSA", admins_inicio, autos_inicio)

print("\nESTADO INICIAL")
parada_universidad.mostrar()

print("\nDEMOSTRACION DE ADICIONAR")

parada_universidad.adicionar("Maria")

parada_universidad.adicionar("Minibus", "Fernando", "MNB-456")

print("\nESTADO FINAL")
parada_universidad.mostrar()