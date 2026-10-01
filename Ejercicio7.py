class KwikEMart:

    def __init__(self):
        # Atributos internos: Listas de objetos ProductoKwikE por pasillo/sección
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []

    def _obtener_pasillo(self, pasillo_nombre):
        """Método auxiliar interno para validar y retornar la lista del pasillo."""
        pasillos = {
            "bebidas": self.bebidas,
            "snacks": self.snacks,
            "conveniencia": self.conveniencia,
        }
        pasillo_lower = pasillo_nombre.lower().strip()
        if pasillo_lower in pasillos:
            return pasillos[pasillo_lower]
        print(" Pasillo '{pasillo_nombre}' no existe. Pasillos válidos: bebidas, snacks, conveniencia."
        )
        return None

    # Métodos para añadir y remover productos

    def agregar_producto(self, pasillo_nombre, producto):
        """Añade un objeto ProductoKwikE a un pasillo específico."""
        pasillo = self._obtener_pasillo(pasillo_nombre)
        if pasillo is not None:
            if isinstance(producto, ProductoKwikE):
                pasillo.append(producto)
                print(" '{producto.descripcion}' añadido al pasillo de {pasillo_nombre.capitalize()"
            else:
                print(" El elemento a agregar debe ser un ProductoKwikE.")

    def remover_producto(self, pasillo_nombre, id_producto):
        """Remueve un producto del pasillo especificado por su ID."""
        pasillo = self._obtener_pasillo(pasillo_nombre)
        if pasillo is not None:
            for i, prod in enumerate(pasillo):
                if prod.id_producto == id_producto:
                    eliminado = pasillo.pop(i)
                 print("{eliminado.descripcion} fue removido de {pasillo_nombre.capitalize()}."
                    )
                    return eliminado
            print("No se encontró ningún producto con ID {id_producto} en el pasillo {pasillo_nombre}."
            )
        return None

    # Métodos para controlar el stock
   

    def ajustar_stock_producto(self, id_producto, nuevo_stock):
        """Busca un producto en todos los pasillos y actualiza su cantidad de stock."""
        todos_los_pasillos = [self.bebidas, self.snacks, self.conveniencia]
        encontrado = False

        for pasillo in todos_los_pasillos:
            for prod in pasillo:
                if prod.id_producto == id_producto:
                    prod.stock = int(nuevo_stock)
                    print("Stock de '{prod.descripcion}' (ID: {id_producto}) actualizado a {nuevo_stock} unidades."
                    )
                    encontrado = True
                    break

        if not encontrado:
            print("No se encontró el producto con ID {id_producto} en ningún pasillo."
            )

    def reporte_inventario(self):
        """Muestra el reporte detallado del inventario actual por cada pasillo."""
        print("\n" + "=" * 45)
        print("INVENTARIO GENERAL DEL KWIK-E-MART  ")
        print("=" * 45)

        pasillos = [
            ("BEBIDAS", self.bebidas),
            ("SNACKS", self.snacks),
            ("CONVENIENCIA", self.conveniencia),
        ]

        for nombre_pasillo, lista_productos in pasillos:
            print(f"\n--- Pasillo: {nombre_pasillo} ---")
            if not lista_productos:
                print("  (Pasillo vacío)")
            else:
                for prod in lista_productos:
                    print(f"  • [ID: {prod.id_producto}] {prod}")
        print("=" * 45 + "\n")
Ejemplos de uso:
Python
# 1. Instanciar la tienda Kwik-E-Mart
tienda = KwikEMart()

# 2. Crear algunos productos
squishee = ProductoKwikE("Squishee", 101, "2026-11-01", precio=3.50, stock=10)
cerveza_duff = ProductoKwikE("Cerveza Duff", 102, "2027-01-15", precio=5.00, stock=24)
donas = ProductoKwikE("Dona Glaseada", 201, "2026-10-05", precio=1.20, stock=30)
revista = ProductoKwikE("Revista Playdude", 301, "2028-01-01", precio=4.50, stock=5)

# 3. Agregar productos a sus respectivos pasillos
tienda.agregar_producto("bebidas", squishee)
tienda.agregar_producto("bebidas", cerveza_duff)
tienda.agregar_producto("snacks", donas)
tienda.agregar_producto("conveniencia", revista)

# 4. Ver el inventario general
tienda.reporte_inventario()

# 5. Ajustar el stock de un producto por ID
tienda.ajustar_stock_producto(id_producto=101, nuevo_stock=25)

# 6. Remover un producto de un pasillo
tienda.remover_producto("conveniencia", id_producto=301)

# 7. Ver el inventario actualizado
tienda.reporte_inventario()
¿Querés agregar alguna otra función a la gestión de la tienda?

Agregar un método para buscar un producto por su ID en toda la tienda

Calcular el valor total monetario en stock del Kwik-E-Mart# 1. Instanciar la tienda Kwik-E-Mart
tienda = KwikEMart()

# 2. Crear algunos productos
squishee = ProductoKwikE("Squishee", 101, "2026-11-01", precio=3.50, stock=10)
cerveza_duff = ProductoKwikE("Cerveza Duff", 102, "2027-01-15", precio=5.00, stock=24)
donas = ProductoKwikE("Dona Glaseada", 201, "2026-10-05", precio=1.20, stock=30)
revista = ProductoKwikE("Revista Playdude", 301, "2028-01-01", precio=4.50, stock=5)

# 3. Agregar productos a sus respectivos pasillos
tienda.agregar_producto("bebidas", squishee)
tienda.agregar_producto("bebidas", cerveza_duff)
tienda.agregar_producto("snacks", donas)
tienda.agregar_producto("conveniencia", revista)

# 4. Ver el inventario general
tienda.reporte_inventario()

# 5. Ajustar el stock de un producto por ID
tienda.ajustar_stock_producto(id_producto=101, nuevo_stock=25)

# 6. Remover un producto de un pasillo
tienda.remover_producto("conveniencia", id_producto=301)

# 7. Ver el inventario actualizado
tienda.reporte_inventario()
# Métodos sobrecargados (Magic Methods)
    

    