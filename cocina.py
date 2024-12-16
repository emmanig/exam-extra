class Cliente:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id

    def realizar_pedido(self, control_de_pedidos, platillo):
        print(f"{self.nombre} realiza un pedido.")
        control_de_pedidos.registrar_pedido(platillo)


class Platillo:
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad

    def validar_existencia(self):
        return self.cantidad > 0


class ControlDePedidos:
    def registrar_pedido(self, platillo):
        if platillo.validar_existencia():
            print(f"Platillo {platillo.nombre} disponible. Pedido registrado.")
        else:
            print(f"Platillo {platillo.nombre} no está disponible.")


# Ejemplo de ejecución
cliente1 = Cliente("Emmanuel", 1)
producto1 = Platillo("enchiladas", 5)
sistema = ControlDePedidos()

cliente1.realizar_pedido(sistema, producto1)
