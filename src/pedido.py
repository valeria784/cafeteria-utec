class Pedido:
    def __init__(self, numero, cliente, producto, cantidad, tipo, tiempo):
        self.numero = numero        # Identificador único
        self.cliente = cliente      # Nombre del cliente
        self.producto = producto    # Alimento o bebida
        self.cantidad = cantidad    # Unidades solicitadas
        self.tipo = tipo            # "Normal" o "Prioritario"
        self.tiempo = tiempo        # Minutos de preparación

    def __str__(self):
        return (f"Pedido #{self.numero} | Cliente: {self.cliente} | "
                f"Producto: {self.producto} | Cantidad: {self.cantidad} | "
                f"Tipo: {self.tipo} | Tiempo: {self.tiempo} min")