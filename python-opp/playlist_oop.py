from canciones import Canciones

class Playlist:

    _total_privadas = 0
    _privadas_por_creador = {}

    def __init__(self, nombre, creador):
        self.__nombre = nombre
        self.__creador = creador
        self.__publica = True
        self.__canciones = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def creador(self):
        return self.__creador

    @property
    def publica(self):
        return self.__publica

    @property
    def total_canciones(self):
        return len(self.__canciones)

    @property
    def duracion_total(self):
        return sum(dur for _, dur in self.__canciones)

    def agregar(self, codigo_cancion):
        if not self.__publica:
            raise ValueError
        info = Canciones.info(codigo_cancion)
        if info is None:
            raise ValueError
        _, _, duracion = info
        self.__canciones.append((codigo_cancion, duracion))

    def hacer_privada(self):
        if not self.__publica:
            raise ValueError
        self.__publica = False
        Playlist._total_privadas += 1
        Playlist._privadas_por_creador[self.__creador] = (
            Playlist._privadas_por_creador.get(self.__creador, 0) + 1
        )

    def __str__(self):
        estado = "Pública" if self.__publica else "Privada"
        return f"Playlist {self.__nombre} de {self.__creador}: {self.total_canciones} canciones - {estado} - {self.duracion_total}s"

    @classmethod
    def total_playlists_privadas(cls):
        return cls._total_privadas

    @classmethod
    def privadas_de(cls, creador):
        return cls._privadas_por_creador.get(creador, 0)
