from asignaturas import Asignaturas

class Matricula:

    _total_cerradas = 0
    _contador_asignaturas = {}

    def __init__(self, id_matricula, estudiante):
        self.__id = id_matricula
        self.__estudiante = estudiante
        self.__cerrada = False
        self.__asignaturas = []

    @property
    def id(self):
        return self.__id

    @property
    def estudiante(self):
        return self.__estudiante

    @property
    def cerrada(self):
        return self.__cerrada

    @property
    def creditos_totales(self):
        return sum(cred for _, cred, _ in self.__asignaturas)

    @property
    def importe_total(self):
        return sum(cred * precio for _, cred, precio in self.__asignaturas)

    def matricular(self, codigo_asignatura):
        if self.__cerrada:
            raise ValueError
        datos = Asignaturas.datos(codigo_asignatura)
        if datos is None:
            raise ValueError
        if codigo_asignatura in [cod for cod, _, _ in self.__asignaturas]:
            raise ValueError
        _, creditos, precio = datos
        if self.creditos_totales + creditos > 30:
            raise ValueError
        self.__asignaturas.append((codigo_asignatura, creditos, precio))

    def cerrar(self):
        if self.__cerrada:
            raise ValueError
        if not self.__asignaturas:
            raise ValueError
        self.__cerrada = True
        Matricula._total_cerradas += 1
        for codigo, _, _ in self.__asignaturas:
            Matricula._contador_asignaturas[codigo] = (
                Matricula._contador_asignaturas.get(codigo, 0) + 1
            )

    def asignaturas_matriculadas(self):
        return [cod for cod, _, _ in self.__asignaturas]

    def __str__(self):
        estado = "Cerrada" if self.__cerrada else "Abierta"
        return (f"Matricula {self.__id} de {self.__estudiante}: "
                f"{len(self.__asignaturas)} asignaturas - {estado} - "
                f"{self.creditos_totales} créditos - Importe {self.importe_total:.2f}€")

    @classmethod
    def total_matriculas(cls):
        return cls._total_cerradas

    @classmethod
    def matriculas_asignatura(cls, codigo_asignatura):
        return cls._contador_asignaturas.get(codigo_asignatura, 0)
