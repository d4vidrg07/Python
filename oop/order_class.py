from productos import Productos

class Pedido:
    # Atributo de clase para contar pedidos cerrados
    __pedidos_cerrados = 0

    def __init__(self, id_pedido, cliente):
        # Atributos privados (encapsulamiento)
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__abierto = True
        self.__lineas = [] # Lista de tuplas (id_producto, cantidad)

    @property
    def id(self):
        return self.__id_pedido

    @property
    def cliente(self):
        return self.__cliente

    @property
    def cerrado(self):
        # Retorna True si NO está abierto
        return not self.__abierto

    @property
    def total(self):
        suma_total = 0.0
        for id_prod, cant in self.__lineas:
            # Obtenemos info del producto usando el método de clase Productos.stock
            info = Productos.stock(id_prod)
            if info:
                # info[1] es el precio según la letra del ejercicio
                suma_total += info[1] * cant
        return suma_total

    def agregar(self, id_producto, cantidad=1):
        # 1. Validar tipo y cantidad
        if not isinstance(cantidad, int) or cantidad < 1:
            raise ValueError("La cantidad debe ser un entero mayor o igual a 1")
        
        # 2. Validar si el pedido está cerrado
        if not self.__abierto:
            raise ValueError("No se pueden añadir productos a un pedido cerrado")
        
        # 3. Validar disponibilidad del producto
        if Productos.stock(id_producto) is None:
            raise ValueError(f"El producto {id_producto} no está disponible")
        
        # Guardamos la línea como una tupla
        self.__lineas.append((id_producto, cantidad))

    def cerrar(self):
        if not self.__abierto:
            raise ValueError("El pedido ya está cerrado")
        if len(self.__lineas) == 0:
            raise ValueError("No se puede cerrar un pedido sin líneas")
        
        self.__abierto = False
        # Acceso al atributo de clase para contabilizar
        Pedido.__pedidos_cerrados += 1

    def lineas_pedido(self):
        # Retorna una copia de la lista de líneas
        return self.__lineas

    @classmethod
    def total_pedidos(cls):
        return cls.__pedidos_cerrados

    def __str__(self):
        estado = "Abierto" if self.__abierto else "Cerrado"
        return (f"Pedido {self.__id_pedido} de {self.__cliente}: "
                f"{len(self.__lineas)} líneas - {estado} - Total {self.total:.2f}€")
