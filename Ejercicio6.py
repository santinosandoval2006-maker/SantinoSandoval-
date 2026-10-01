# Métodos sobrecargados (Magic Methods)
    def __str__(self):
        """Representación legible del producto (Descripción y Precio)."""
        return f"Producto: {self.descripcion} | Precio: ${self.precio:.2f}"

    def __eq__(self, otro):
        """Compara si dos productos son iguales basándose en su ID y descripción."""
        if isinstance(otro, ProductoKwikE):
            return (
                self.id_producto == otro.id_producto
                and self.descripcion == otro.descripcion
            )
        return False# 1. Crear productos para probar
prod1 = ProductoKwikE(
    "Squishee de Menta", 101, "2026-10-10", precio=3.50, stock=15
)
prod2 = ProductoKwikE(
    "Squishee de Menta", 101, "2026-12-01", precio=4.00, stock=50
)
prod3 = ProductoKwikE(
    "Dona Rosada", 102, "2026-10-10", precio=1.50, stock=20
)

# 2. Prueba del método __str__ (se activa con print o str())
print("--- Representación legible (__str__) ---")
print(prod1)  # Output: Producto: Squishee de Menta | Precio: $3.50
print(prod3)  # Output: Producto: Dona Rosada | Precio: $1.50

# 3. Prueba del método __eq__ (se activa con ==)
print("\n--- Comparación de productos (__eq__) ---")
print(
    f"¿prod1 es igual a prod2? {prod1 == prod2}"
)  # True (mismo ID: 101 y descripción)
print(f"¿prod1 es igual a prod3? {prod1 == prod3}")  # False (distinto ID y desc)
