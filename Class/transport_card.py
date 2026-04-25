class TarjetaTransporte:
    contador = 1000001
    _todas_las_tarjetas = []

    def __init__(self, titular):
        self._titular = titular
        self._saldo = 0.0
        self._viajes_realizados = 0

        self._numero_tarjeta = f'TT-{TarjetaTransporte.contador}'
        TarjetaTransporte.contador += 1
        TarjetaTransporte._todas_las_tarjetas.append(self)

    @property
    def numero_tarjeta(self):
        return self._numero_tarjeta
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def viajes_realizados(self):
        return self._viajes_realizados
    

    def recargar(self, cantidad):
        if cantidad <= 0:
            raise ValueError
        self._saldo += cantidad
        
    def viajar(self, costo_viaje):
        if costo_viaje < 0:
            raise ValueError
        if self._saldo < costo_viaje:
            raise ValueError
        self._saldo -= costo_viaje
        self._viajes_realizados += 1


    @classmethod
    def total_tarjetas_emitidas(cls):
        return len(cls._todas_las_tarjetas)    #solo quiere saber la cantidad
    @classmethod
    def viajes_titular(cls, nombre_titular):
        total_viajes = 0
        for tarjeta in cls._todas_las_tarjetas:
            if tarjeta.titular == nombre_titular:
                total_viajes += tarjeta.viajes_realizados
        return total_viajes
    
    def __str__(self):
        return f'{self._numero_tarjeta} - Titular: {self._titular}, Saldo: {self._saldo}, Viajes: {self._viajes_realizados}'


