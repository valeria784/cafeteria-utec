from collections import deque
from src.pedido import Pedido


class Cafeteria:
    def __init__(self):
        self.fila_normal = deque()        # Cola FIFO de pedidos normales
        self.fila_prioritaria = deque()   # Cola FIFO de pedidos prioritarios
        self.contador = 1                 # Para generar números únicos
        self.total_registrados = 0
        self.total_cancelados = 0
        self.preparados = []              # Lista de pedidos ya preparados

    # 1. Registrar pedido
    def registrar_pedido(self, cliente, producto, cantidad, tipo, tiempo):
        pedido = Pedido(self.contador, cliente, producto, cantidad, tipo, tiempo)
        self.contador += 1
        self.total_registrados += 1

        if tipo == "Prioritario":
            self.fila_prioritaria.append(pedido)
        else:
            self.fila_normal.append(pedido)
        return pedido

    # 3. Consultar el siguiente pedido (sin sacarlo de la fila)
    def consultar_siguiente(self):
        if self.fila_prioritaria:
            return self.fila_prioritaria[0]
        if self.fila_normal:
            return self.fila_normal[0]
        return None

    # 2. Preparar el siguiente pedido (primero la fila prioritaria)
    def preparar_siguiente(self):
        if self.fila_prioritaria:
            pedido = self.fila_prioritaria.popleft()
        elif self.fila_normal:
            pedido = self.fila_normal.popleft()
        else:
            return None
        self.preparados.append(pedido)
        return pedido

    # 4. Mostrar pedidos pendientes
    def pedidos_pendientes(self):
        return list(self.fila_prioritaria), list(self.fila_normal)

    # 6. Cancelar pedido por número
    def cancelar_pedido(self, numero):
        for fila in (self.fila_prioritaria, self.fila_normal):
            for pedido in fila:
                if pedido.numero == numero:
                    fila.remove(pedido)
                    self.total_cancelados += 1
                    return pedido
        return None

    # 5. Estadísticas
    def estadisticas(self):
        total_preparados = len(self.preparados)
        tiempo_total = sum(p.tiempo for p in self.preparados)
        promedio = tiempo_total / total_preparados if total_preparados > 0 else 0

        return {
            "registrados": self.total_registrados,
            "preparados": total_preparados,
            "cancelados": self.total_cancelados,
            "pendientes_prioritarios": len(self.fila_prioritaria),
            "pendientes_normales": len(self.fila_normal),
            "tiempo_total": tiempo_total,
            "tiempo_promedio": promedio,
        }