# Clase base para el manejo de datos
class RegistroDatos:
    def __init__(self):
        self.datos = []

    def registrar(self, dato):
        self.datos.append(dato)
        print(f"Datos registrados: {dato}")

    def mostrar_datos(self):
        return self.datos

# Clase Cliente
class Cliente:
    def __init__(self, nombre_cliente, id_cliente):
        self.nombre_cliente = nombre_cliente
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self.nombre_cliente} (ID: {self.id_cliente})"

# Clase Pedido (hereda RegistroDatos)
class Pedido(RegistroDatos):
    def __init__(self):
        super().__init__()

    def agregar_pedido(self, cliente, detalle_pedido):
        pedido = {"cliente": cliente, "detalle": detalle_pedido}
        self.registrar(pedido)

# Clase Informe (hereda RegistroDatos)
class Informe(RegistroDatos):
    def __init__(self):
        super().__init__()

    def generar_informe(self):
        print("\nGenerando informe de pedidos...")
        for index, registro in enumerate(self.datos, 1):
            print(f"{index}. Cliente: {registro['cliente'].nombre_cliente}, Detalle: {registro['detalle']}")

# Clase ControlPedidos (para manejar operaciones de pedidos)
class ControlPedidos:
    def __init__(self):
        self.pedidos = Pedido()

    def realizar_pedido(self, cliente, detalle):
        print(f"\nRealizando pedido para {cliente.nombre_cliente}")
        self.pedidos.agregar_pedido(cliente, detalle)

    def mostrar_pedidos(self):
        return self.pedidos.mostrar_datos()

# Función principal
def main():
    # Crear objetos
    cliente1 = Cliente("Juan Pérez", 1)
    cliente2 = Cliente("María López", 2)
    
    control_pedidos = ControlPedidos()
    informe = Informe()

    # Simulación de pedidos
    control_pedidos.realizar_pedido(cliente1, "2 Productos: Laptop, Teclado")
    control_pedidos.realizar_pedido(cliente2, "1 Producto: Monitor")

    # Guardar pedidos en el informe
    for pedido in control_pedidos.mostrar_pedidos():
        informe.registrar(pedido)

    # Generar informe
    informe.generar_informe()

if __name__ == "__main__":
    main()
