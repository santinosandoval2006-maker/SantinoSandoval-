
class ProductoKwikE:

    def __init__(self, descripcion, id_producto, fecha_vencimiento, precio, stock):
        self.descripcion = str(descripcion)
        self.id_producto = int(id_producto)

        # Acepta instancias de date/datetime o cadenas 'YYYY-MM-DD'
        if isinstance(fecha_vencimiento, str):
            self.fecha_vencimiento = datetime.strptime(
                fecha_vencimiento, "%Y-%m-%d"
            ).date()
        elif isinstance(fecha_vencimiento, datetime):
            self.fecha_vencimiento = fecha_vencimiento.date()
        else:
            self.fecha_vencimiento = fecha_vencimiento

        self.precio = float(precio)
        self.stock = int(stock)

    def actualizar_datos(self, **kwargs):
        """Permite modificar uno o varios atributos del producto pasándolos como argumentos de palabra clave (ej.

        precio=12.50, stock=10).
        """
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                if clave == "fecha_vencimiento" and isinstance(valor, str):
                    valor = datetime.strptime(valor, "%Y-%m-%d").date()
                setattr(self, clave, valor)
            else:
                print("El atributo '{clave}' no existe en el producto.")

    def dias_para_expirar(self, fecha_referencia=None):
        """Calcula cuántos días faltan para que el producto expire.

        Si ya expiró (o expira hoy), alerta al usuario y coloca el stock en 0.
        """
        if fecha_referencia is None:
            fecha_referencia = date.today()
        elif isinstance(fecha_referencia, str):
            fecha_referencia = datetime.strptime(
                fecha_referencia, "%Y-%m-%d"
            ).date()

        dias_restantes = (self.fecha_vencimiento - fecha_referencia).days

        if dias_restantes <= 0:
            print("¡ALERTA Apu! El producto '{self.descripcion}' (ID: {self.id_producto}) ha EXPIRADO."
            )
            self.stock = 0

        return dias_restantes

    def __repr__(self):
        return (
            f"ProductoKwikE(id={self.id_producto}, desc='{self.descripcion}', "
            f"precio=${self.precio}, stock={self.stock}, vence={self.fecha_vencimiento})"
        )

# 1. Crear un producto
squishee = ProductoKwikE(
    descripcion="Squishee de Menta",
    id_producto=101,
    fecha_vencimiento="2026-10-10",
    precio=3.50,
    stock=20,

print("Producto inicial:")
print(squishee)

# 2. Modificar varios datos de forma fácil
squishee.actualizar_datos(precio=4.00, stock=15)
print("\nDespués de actualizar precio y stock:")
print(squishee)

# 3. Calcular días para expirar (ejemplo con fecha futura)
dias = squishee.dias_para_expirar(fecha_referencia="2026-10-05")
print(f"\nDías faltantes para expirar: {dias}")

# 4. Verificar cuando ya está vencido (activa alerta y pone el stock en 0)
print("\nComprobando expiración al llegar la fecha:")
squishee.dias_para_expirar(fecha_referencia="2026-10-11")
print(squishee)