class CuentaBancaria:
    __cuentas_totales = 0
    __cuentas_titulares = []
    def __init__(self, titular):
        CuentaBancaria._cuentas_totales += 1
        self.__titular =  titular
        self.__saldo = 0.0

        self.__codigo_cuenta = f'CB-{CuentaBancaria.__cuentas_totales:03d}'
        CuentaBancaria.__cuentas_titulares.append(self)
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def codigo_cuenta(self):
        return self.__codigo_cuenta
    
    def depositar(self, cantidad):
        if cantidad < 0:
            raise ValueError('Cantidad Negativa')
        else:
            self.__saldo += cantidad

    def retirar(self, cantidad):
        if cantidad < 0:
            raise ValueError('Cantidad negativa')
        if cantidad > self.__saldo:
            raise ValueError('No tienes tanto dinero')
        else:
            self.__saldo -= cantidad

    @classmethod
    def obtener_total_cuentas(cls):
        return CuentaBancaria._cuentas_totales
    
    @classmethod
    def total_saldo_titular(cls, titular):
        total_saldo = 0.0
        for cuenta in cls.__cuentas_titulares:
            if cuenta.titular == titular:
                total_saldo += cuenta.saldo
        return total_saldo





