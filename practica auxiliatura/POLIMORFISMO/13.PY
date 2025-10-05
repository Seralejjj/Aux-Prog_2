import math

class Mp4:
    def __init__(self, marca: str, capacidadGb: float, canciones_data: list, videos_data: list):
        self.marca = marca
        self.capacidadGb = capacidadGb
        
        self.canciones = canciones_data
        self.nroCanciones = len(self.canciones[0]) if self.canciones and self.canciones[0] else 0
        
        self.videos = videos_data
        self.nroVideos = len(self.videos)
        
        print(f"Mp4 '{self.marca}' inicializado con {self.capacidadGb} GB.")

    def convertir_peso_a_gb(self):
        peso_canciones_kb = sum(self.canciones[2]) if self.nroCanciones > 0 else 0
        peso_canciones_gb = peso_canciones_kb / (1024 * 1024) 
        
        peso_videos_mg = sum(video[2] for video in self.videos) if self.nroVideos > 0 else 0
        peso_videos_gb = peso_videos_mg / 1024 
        
        return peso_canciones_gb + peso_videos_gb

    def mostrarCapacidad(self):
        peso_usado = self.convertir_peso_a_gb()
        disponible = self.capacidadGb - peso_usado
        print(f"Capacidad total: {self.capacidadGb:.2f} GB")
        print(f"Capacidad usada: {peso_usado:.4f} GB")
        print(f"Capacidad disponible: {disponible:.4f} GB")
        return disponible

    def _borrar_cancion_por_indice(self, indice):
        if 0 <= indice < self.nroCanciones:
            nombre = self.canciones[0].pop(indice)
            self.canciones[1].pop(indice)
            self.canciones[2].pop(indice)
            self.nroCanciones -= 1
            print(f"Cancion '{nombre}' eliminada.")
            return True
        return False

    def borrar(self, param1, param2=None):
        if param2 is None:
            try:
                indice_nombre = self.canciones[0].index(param1)
                return self._borrar_cancion_por_indice(indice_nombre)
            except ValueError:
                pass 
            try:
                indice_artista = self.canciones[1].index(param1)
                return self._borrar_cancion_por_indice(indice_artista)
            except ValueError:
                pass 
            
            print(f"Advertencia: No se encontro cancion con nombre/artista '{param1}'.")
            return False

        else:
            nombre = param1
            peso = param2
            for i in range(self.nroCanciones):
                if self.canciones[0][i] == nombre and self.canciones[2][i] == peso:
                    return self._borrar_cancion_por_indice(i)
            print(f"Advertencia: No se encontro cancion '{nombre}' con peso {peso} KB.")
            return False

    def __add__(self, nueva_cancion: list):
        nombre, artista, peso = nueva_cancion[0], nueva_cancion[1], nueva_cancion[2]
        
        for i in range(self.nroCanciones):
            if self.canciones[0][i] == nombre and self.canciones[1][i] == artista:
                print(f"ERROR (+): Cancion '{nombre}' ya existe en el Mp4.")
                return self

        peso_cancion_gb = peso / (1024 * 1024)
        if self.mostrarCapacidad() < peso_cancion_gb:
            print(f"ERROR (+): Espacio insuficiente para '{nombre}'.")
            return self

        self.canciones[0].append(nombre)
        self.canciones[1].append(artista)
        self.canciones[2].append(peso)
        self.nroCanciones += 1
        print(f"Cancion '{nombre}' adicionada. Nuevo total: {self.nroCanciones}")
        return self

    def __sub__(self, nuevo_video: list):
        nombre, artista, peso = nuevo_video[0], nuevo_video[1], nuevo_video[2]
        
        for video in self.videos:
            if video[0] == nombre and video[1] == artista:
                print(f"ERROR (-): Video '{nombre}' ya existe en el Mp4.")
                return self

        peso_video_gb = peso / 1024
        if self.mostrarCapacidad() < peso_video_gb:
            print(f"ERROR (-): Espacio insuficiente para video '{nombre}'.")
            return self

        self.videos.append(nuevo_video)
        self.nroVideos += 1
        print(f"Video '{nombre}' adicionado. Nuevo total: {self.nroVideos}")
        return self

CANCIONES_INIT = [
    ["Back To Black", "Lost On You"], 
    ["Amy Winehouse", "LP"],        
    [100, 150]                      
]

VIDEOS_INIT = [
    ["Heathens", "twenty one pilots", 50],
    ["Harmonica Andromeda", "KSHMR", 70]
]

mp4 = Mp4("IPod-UMSA", 1.0, CANCIONES_INIT, VIDEOS_INIT)

print("\n D) CAPACIDAD INICIAL")
mp4.mostrarCapacidad()

print("\n B) SOBRECARGA + (ADICIONAR CANCION)")

mp4 = mp4 + ["Calculo I", "Gemini", 1000]

mp4 = mp4 + ["Lost On You", "LP", 150]

print("\n C) SOBRECARGA - (ADICIONAR VIDEO)")

mp4 = mp4 - ["Without Me", "Halsey", 30]

print("\n D) CAPACIDAD DESPUES DE ADICIONES ")
mp4.mostrarCapacidad()

print("\n A) POLIMORFISMO EN BORRAR ")

mp4.borrar("Calculo I")

mp4.borrar("LP")

mp4.borrar("Heathens", 50)