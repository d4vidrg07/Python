#########################################################
#                                                       #
#   __  __  ____  _      _____  ______                  #
#  |  \/  |/ __ \| |    |  __ \|  ____|                 #
#  | \  / | |  | | |    | |  | | |__                    #
#  | |\/| | |  | | |    | |  | |  __|                   #
#  | |  | | |__| | |____| |__| | |____                  #
#  |_|  |_|\____/|______|_____/|______|                 #
#                                                       #
#             ¡MOLDE, NO TOCAR!                         #
#                                                       #
#########################################################


#EMPIEZA CON MOSTRAR PARA VERLO

#voy a intentar hacer todo en una Liked list sort, todo lo que me puedan pedri
#---------------------
#añadir numeros final
#añadir numeros principio
#añadir numeros donde quieras
#---------------------
#mostrar numeros
#sumar numeros
#---------------------
#borrar numeros final
#borrar numeros principio
#borrar numeros donde quieras

#-------------------
#Devoler el primero y actualizar

#---VI EN EXAMENES-----
#Conectar nodos pares en una lista origianl
#nodos impares en una lista nueva

#tambien; hacer un @property con algo puesto en el init 

#vi algo tambien donde si lo que encontrabas era de un tipo, pon tu str borrar todos los str

#poner en orden numerico

#si numero == a valor borrar

#contendor de size

#recibir un grupo y unión de miembros del grupo actual 
# y el grupo recibido por parámetro (sin duplicados).


class Client:
    def __init__(self, name, total_cost):
        self.name = name
        self.total_cost = total_cost
        # TIP: Aquí podrías añadir el @property que mencionaste

    def __str__(self):
        return f"{self.name}: {self.total_cost}"

class MyList():
    class Node:
        def __init__(self, value, next=None):
            self.value = value
            self.next = next

    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0
        

    # --- AÑADIR ---
    def add_al_principio(self, value):
        new_node = self.Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            #NEW NODE .NEXT, AHI PONEMOS EL FIRST
            new_node.next = self.first
            self.first = new_node
            
        self._size += 1

    #para saber desepquetar (por si acaso) añado 1 condicion mas
    def add_al_final(self, value):
        new_node = self.Node(value)
        #si no hay nada
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self._size += 1

    def add_ordenado(self, value):
        #REHACER
        #nuevo nodo
        new_node = self.Node(value)
        #si nada
        if self.first is None:
            self.add_al_principio(value)
            return
        #si es el mas peuqeño
        elif self.first.value > value:
            self.add_al_principio(value)
            return
        else:
            puntero = self.first
            while puntero.next is not None and puntero.next.value < value:
                puntero = puntero.next
            #si es el mas grande
            if puntero.next is None:
                self.add_al_final(value)
            #si no
            else:
                #el siguiente del nodo, debe ser el siiguiente del putnero
                new_node.next = puntero.next
                puntero.next = new_node
                self._size += 1
            

    def add_en_posicion(self, value, index):
        #nodo:
        new_node = self.Node(value)
        #index invalido
        if index < 0 or index > self._size:
            print("Index invalido")
            return
        elif index == 0:
                self.add_al_principio(value)
        elif index == self._size:
                self.add_al_final(value)
        #si no
        else:
            puntero = self.first
            i = 0
            while puntero is not None and i < index-1:
                puntero = puntero.next
                i += 1
            
            new_node.next = puntero.next
            puntero.next = new_node
            self._size += 1
        

    #propiedad llamda size que tendra la cantidad de numeros, devera ser actualizada en todos los add y todos los del
    @property
    def size(self):
        return self._size
    # --- MOSTRAR Y CÁLCULOS ---
    #mostrar numeros
    #demasiado pro, solo ver bine
    def mostrar(self):
        if self.first is None:
            print("Empty List: [None]")
            return
        
        elementos = []
        puntero = self.first
        while puntero is not None:
            # Si el valor es un objeto Client, usamos su __str__, si no, el valor tal cual
            val = str(puntero.value)
            elementos.append(f"[{val}]")
            puntero = puntero.next
        
        # Unimos con flechas y añadimos el None final para que parezca un esquema real
        esquema = " -> ".join(elementos) + " -> None"
        print(esquema)
            

    #sumar valores
    def sumar_valores(self):
        suma = 0
        puntero = self.first
        while puntero is not None:
            suma += puntero.value
        
        return suma
    
    #propiedad size
    @property
    def size(self):
        return self._size

    # --- BORRAR ---
    def borrar_principio(self):
        if self.first is None:
            return None
            
        elemento_extraer = self.first.value
        
        self.first = self.first.next
        self._size -= 1
        
        if self.first is None:
            self.last = None
        
        return elemento_extraer
        
    def borrar_final(self):
        if self.first is None:
            return None
        elif self.first == self.last:
            devolver = self.first.value
            self.first = self.last = None
            return devolver
        else:
            puntero = self.first
            while puntero.next.next is not None:
                puntero = puntero.next
                
            puntero.next = None
            self.last = puntero
            self._size -= 1

    def borrar_posicion(self, index):
        if index < 0 or index > self.size:
            print("FUERA DE RANGO")
            return
        elif index == 0:
            return None
        else:
            puntero = self.first
            i = 0
            while i < index-1:
                puntero = puntero.next
                i += 1
            
            puntero.next = puntero.next.next
            if puntero.next is None:
                self.last = puntero
            
            self._size -= 1
            
        
    def borrar_por_valor(self, valor):
        # Si numero == a valor borrar
        if self.first is None:
            return None
        while self.first.value == valor and self.first is not None:
            self.borrar_principio()
        else:
            puntero = self.first
            while puntero.next is not None and puntero.next.value != valor:
                puntero = puntero.next
            if puntero.next is None:
                print("valor no existe")
                pass
            else:
                puntero.next = puntero.next.next
                if puntero.next is None:
                    self.last = puntero
                self._size -= 1
            
                    

    def borrar_por_tipo(self, tipo_a_borrar):
        # Ejemplo: borrar todos los str
        if self.first is None:
            return None
        #por si al prinicio
        while type(self.first.value) == tipo_a_borrar and self.first is not None:
            self.borrar_principio()
        #si no
        else:
            puntero = self.first
            while puntero.next is not None and type(puntero.next.value) != tipo_a_borrar:
                puntero = puntero.next
                #si no esta el tipo
                if puntero.next is None:
                    print("tipo no enocntrado")
                    pass
                else:
                    puntero.next = puntero.next.next
                    if puntero.next is None:
                        self.last = puntero
                    self._size -= 1
            

    # --- EXAMEN: FILTRADO Y GRUPOS ---
    def split(self):
        """
        Mantiene los pares en la original y 
        devuelve una lista nueva con los impares.
        """
        nueva_lista = MyList()
        return nueva_lista

    def union(self, otra_lista):
        """
        Unión de miembros del grupo actual y el recibido
        sin duplicados.
        """
        pass

    def true_size(self):
        """ De manera verdadera (mediante, bucles) calcularas el tamaño de la lista"""
    
    def iter(self):
        puntero = self.first
        while puntero:
            yield puntero.value
            puntero = puntero.next
    
    #ENTORNO PRUEBAS
    # ==========================================
# ENTORNO DE PRUEBAS (Debug)
# ==========================================
if __name__ == "__main__":
    print("--- 🧪 Iniciando Pruebas de la Lista ---")
    mi_lista = MyList()

    # 1. Probar Añadir
    print("\n1. Añadiendo elementos...")
    mi_lista.add_al_principio(10)
    mi_lista.add_al_final(20)
    mi_lista.add_al_final(30)
    mi_lista.add_al_principio(5)
    mi_lista.add_en_posicion(500, 1)  # Debería insertar el 15 entre el 10 y el 20

    # Lista esperada: 5 -> 10 -> 20 -> 30
    mi_lista.mostrar()

    # 2. Probar Size y Suma
    print(f"\n2. Tamaño actual: {mi_lista.size}")
    print(f"Suma total: {mi_lista.sumar_valores()}")
    # 3. Probar Borrado
    print("\n3. Borrando principio...")
    borrado = mi_lista.borrar_principio()
    print(f"Elemento extraído: {borrado}")
    mi_lista.mostrar() # Debería empezar en 10
#    # 4. Probar @property en Client
    print("\n4. Probando objetos Client...")
    c1 = Client("Ana", 50)
    c2 = Client("Pepe", 30)
    lista_clientes = MyList()
    lista_clientes.add_al_final(c1)
    lista_clientes.add_al_final(c2)
    lista_clientes.mostrar()
    # Si hiciste el @property cost, esto debería funcionar:
    print(f"Coste del primer cliente: {lista_clientes.first.value.cost}")
#    # 5. Probar Orden Numérico
    print("\n5. Probando añadir ordenado...")
    lista_ordenada = MyList()
    lista_ordenada.add_ordenado(50)
    lista_ordenada.add_ordenado(10)
    lista_ordenada.add_ordenado(30)
    lista_ordenada.mostrar() # Debería ser 10 -> 30 -> 50
    # 9. Probar Borrar Final
    print("\n9. Probando borrar_final...")
    test_borrar = MyList()
    test_borrar.add_al_final(100)
    test_borrar.add_al_final(200)
    test_borrar.add_al_final(300)
    
    print("Lista original:")
    test_borrar.mostrar() # 100 -> 200 -> 300
    
    ultimo = test_borrar.borrar_final()
    print(f"Eliminado: {ultimo} (Debe ser 300)")
    print("Tras borrar el final:")
    test_borrar.mostrar() # 100 -> 200
    
    print(f"Nuevo 'last' de la lista: {test_borrar.last.value} (Debe ser 200)")
    
    test_borrar.borrar_final() # Borra el 200
    test_borrar.borrar_final() # Borra el 100 (La lista queda vacía)
    
    print(f"Tamaño final: {test_borrar.size} (Debe ser 0)")
    test_borrar.mostrar() # Debe decir "Lista vacía"

    # --- DEBUG RÁPIDO: borrar_posicion ---
    print("\n--- 🧪 Test borrar_posicion ---")
    debug_lista = MyList()
    for x in [10, 20, 30, 40]: debug_lista.add_al_final(x)
    
    # 1. Caso Normal (Intermedio)
    print("Original: ", end=""); debug_lista.mostrar()
    print(f"Borrando índice 1 (valor 20)...")
    debug_lista.borrar_posicion(1)
    debug_lista.mostrar() # 10 -> 30 -> 40
    
    # 2. Caso Límite (Error de rango)
    print(f"\nProbando índice fuera de rango (-5):")
    try:
        debug_lista.borrar_posicion(-5)
    except Exception as e:
        print(f"Error capturado: {e}")
    
    print(f"\nEstado final: Size {debug_lista.size}, Last {debug_lista.last.value}")
        
    # --- DEBUG RÁPIDO: borrar_por_valor ---
    print("\n--- 🧪 Test borrar_por_valor ---")
    lista_val = MyList()
    for x in [5, 10, 15]: lista_val.add_al_final(x)
    
    # 1. Caso Normal: Borrar el 10
    print("Original: ", end=""); lista_val.mostrar()
    lista_val.borrar_por_valor(10)
    print("Tras borrar 10: ", end=""); lista_val.mostrar() # 5 -> 15
    
    # 2. Caso Error: Valor inexistente
    print("\nBorrando valor 99:")
    try:
        lista_val.borrar_por_valor(99)
    except Exception as e:
        print(f"Resultado: {e}")
    
    # Verificación de punteros
    print(f"Final -> First: {lista_val.first.value}, Last: {lista_val.last.value}")
    # 6. Probar Filtro Pares/Impares
    print("\n6. Probando separación pares/impares...")
    numeros = MyList()
    for i in range(1, 7): numeros.add_al_final(i)
    print("Original:")
    numeros.mostrar()
    impares = numeros.split()
    print("Solo pares (original modificada):")
    numeros.mostrar()
    print("Solo impares (nueva lista):")
    impares.mostrar()
    # 7. Probar Borrado por Tipo
    print("\n7. Probando borrar por tipo (ej. borrar strings)...")
    mezcla = MyList()
    mezcla.add_al_final(10)
    mezcla.add_al_final("BORRAME")
    mezcla.add_al_final("BORRAME TAMBIEN")
    mezcla.add_al_final(20)
    mezcla.mostrar()
    mezcla.borrar_por_tipo(str)
    
    # 8. Probar Unión sin duplicados
    print("\n8. Probando unión de grupos...")
    g1 = MyList()
    g1.add_al_final(1)
    g1.add_al_final(2)
    g2 = MyList()
    g2.add_al_final(2) # Duplicado
    g2.add_al_final(3)
    g1.union(g2)
    print("Unión (debe ser 1, 2, 3):")
    g1.mostrar()
    
    
    # ==========================================
    # TEST: Integridad del Tamaño (true_size)
    # ==========================================
    print("\n--- 🧪 Probando true_size vs _size ---")
    lista_test = MyList()
    
    # 1. Caso lista vacía
    print(f"Lista vacía -> Atributo _size: {lista_test._size}, Real (true_size): {lista_test.true_size()}")
    
    # 2. Añadiendo elementos
    for x in [10, 20, 30, 40]: 
        lista_test.add_al_final(x)
    
    print(f"Tras añadir 4 -> Atributo _size: {lista_test._size}, Real (true_size): {lista_test.true_size()}")
    
    # 3. Forzamos un desajuste manual para ver si true_size no miente
    print("\n[Debug] Simulando un error manual en el contador...")
    lista_test._size = 99  # Mentimos al atributo
    print(f"Atributo (Mentira): {lista_test._size}")
    print(f"Realidad (true_size): {lista_test.true_size()}  <-- Debería seguir siendo 4")
    
    # 4. Sincronizamos
    lista_test._size = lista_test.true_size()
    print(f"Sincronizado de nuevo: {lista_test._size}")
    
    
    print("\n--- ✅ Pruebas finalizadas ---")
    
